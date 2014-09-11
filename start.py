import os
os.system('clear')
import json
import importlib
import argparse
import gevent
import requests
from gevent.threadpool import ThreadPool
from gevent.queue import Queue
from gevent import monkey
monkey.patch_all(thread=False)


input_file = None
threads_count = 0

global_headers = {}
global_post_param = {}
global_query_param = {}
domain = ''
tasks = Queue()


def get_input():
    try:
        global input_file, threads_count
        parser = argparse.ArgumentParser()
        parser.add_argument('--input', help='testcase json file as input')
        parser.add_argument('--threads', help='Thread Pool size (integer)')
        input_file = parser.parse_args().input
        threads_count = int(parser.parse_args().threads)
    except Exception as e:
        print 'Wrong input --help for help : Error(' + str(e) + ')'
        exit(1)
    if input_file is None or threads_count is None:
        print 'Wrong input --help for help'
        exit(1)


def complete_task(test):
    request = test.TEST['request']
    if 'hooks' in test.TEST:
        test.TEST['request']['hooks'](request)

    if '://' not in request['url']:
        request['url'] = domain + request['url']

    response = requests.Session().request(request['method'], request['url'],
                                          request.get('params'), request.get('data'),
                                          request.get('headers'), request.get('cookies'),
                                          request.get('files'), request.get('auth'),
                                          request.get('timeout'), request.get('allow_redirects', True),
                                          request.get('proxies'), request.get('hooks'),
                                          request.get('stream'), request.get('verify'), request.get('cert'))

    if 'hook' in test.TEST['response']:
        return test.TEST['response']['hooks'](response)
    else:
        if 'status_code' in test.TEST['response'] and response.status_code != test.TEST['response']['status_code']:
            return False
        if 'body' in test.TEST['response'] and response.content != test.TEST['response']['body']:
            return False
        if 'header' in test.TEST['response']:
            for h in test.TEST['response']['headers']:
                if response.headers.get(h, None) == None:
                    return False
                elif response.headers[h] != test.TEST['response'][h]:
                    return False
    return True


def worker():
    while not tasks.empty():
        task = tasks.get()
        test = importlib.import_module(task[:task.find('.py')])
        print '========================================================================'
        print 'Starting Test:', test.TEST['name']
        if complete_task(test) is False:
            print test.TEST['name'], 'Test Failed'
            return

        print test.TEST['name'], 'Test Sucess'


if __name__ == '__main__':
    get_input()

    test_suite = importlib.import_module(input_file[:input_file.find('.py')])
    print '========================================================================'
    print 'Test Suite Project Name:', test_suite.TEST['project_name']

    if 'init_hooks' in test_suite.TEST:
        test_suite.TEST['init_hooks'](global_headers, global_post_param, global_query_param)
    domain = '%s://%s' % (test_suite.TEST['protocol'], test_suite.TEST['domain'])

    for i in range(0, len(test_suite.TEST['testcases'])):
        tasks.put_nowait(test_suite.TEST['testcases'][i])

    pool = ThreadPool(threads_count)
    for _ in range(threads_count):
        pool.spawn(worker)

    pool.join()