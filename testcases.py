def init_handler(global_headers, global_post_param, global_query_param):
    global_headers['X-REST-API'] = 'testing'
    global_post_param['rest'] = 'api'
    global_query_param['type'] = 'test'


TEST = {
    'project_name': 'CloudMagic Gamma - Sync APIs',
    'global_headers': {},
    'global_post_param': {},
    'global_query_param': {},
    'init_hooks': init_handler,
    'domain': 'www.example.com',
    'protocol': 'http',
    'testcases': [
        'test_ews_push.py',
    ]
}
