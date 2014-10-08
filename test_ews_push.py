def handler(response):
    print 'handler'
    TEST['request'][1]['url'] = '/xyz/fdsa'
    return True


#<request>
'''self, method, url,
        params=None,
        data=None,
        headers=None,
        cookies=None,
        files=None,
        auth=None,
        timeout=None,
        allow_redirects=True,
        proxies=None,
        hooks=None,
        stream=None,
        verify=None,
        cert=None'''


TEST = {
        'name': 'Sample Test 1',
        'request': [
        {
                'method': 'POST',
                #'url': '/sample/get1',
                #'params': {'key': 'value'},
                #'data': {'key': 'value'},
		'url':'http://127.0.0.1:1200?user_id=862399&account_id=2',
		'query_string': {'user_id':'862399','account_id':'2'},
                'timeout': 60,
		'data' : '<?xml version="<soap11:Envelope xmlns:soap11="http://schemas.xmlsoap.org/soap/envelope/"><soap11:Header><t:RequestServerVersion xmlns:m="http://schemas.microsoft.com/exchange/services/2006/messages" Version="Exchange2010" xmlns:t="http://schemas.microsoft.com/exchange/services/2006/types" /></soap11:Header><soap11:Body><m:SendNotification xmlns:t="http://schemas.microsoft.com/exchange/services/2006/types" xmlns:m="http://schemas.microsoft.com/exchange/services/2006/messages"><m:ResponseMessages><m:SendNotificationResponseMessage ResponseClass="Success"><m:ResponseCode>NoError</m:ResponseCode><m:Notification><t:SubscriptionId>GABtYWlsLmV4Y2hhbmdlLndlYnlvZy5jb20QAAAAmzjJwJ17LEWXFJ3elwB78yMLCAwpsNEI</t:SubscriptionId><t:PreviousWatermark>AQAAAAr+ALjCIXZKoQcwbiGBIH4HHicDAAAAAAA=</t:PreviousWatermark><t:MoreEvents>false</t:MoreEvents><t:StatusEvent><t:Watermark>AQAAAAr+ALjCIXZKoQcwbiGBIH43HicDAAAAAAE=</t:Watermark></t:StatusEvent></m:Notification></m:SendNotificationResponseMessage></m:ResponseMessages></m:SendNotification></soap11:Body></soap11:Envelope>'
                #'headers': {'key': 'value'}
        }
        ],
        'response': [
        {
                'http_status': 200,
                #'body': 'result',
                #'header': {'key': 'value'},
                #'hooks': handler
        }
        ]
}



