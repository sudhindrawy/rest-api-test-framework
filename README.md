rest-api-test-framework
=======================
This is a generic REST API test framework written in python. 

To run
> python start.py --input testcases.json

Sample testcases.json
===============================================================================
{
"project_name": "CloudMagic Gamma - Sync APIs",
"handler_modules": ["sampletest"],
"global_headers": {},
"global_post_param": {},
"global_query_param": {},
"init_handler_callback": "init_handler",
"test_cases": [
		{
		"name": "Sample Test 1",
		"timeout": 60,
		"request" : {
				"type": "POST",
				"end_point":"/sample/post",
				"post_param": {"key":"value"},
				"query_param": {"key":"value"},
				"headers": {"key":"value"}
			     },
		"response" : {
				"http_status": 200,
				"body": {"key":"value"},
				"header": {"key":"value"},
				"handler_callback": "search_handler"
			     }
		},
		{
		"name": "Sample Test 2",
		"timeout": 60,
		"request" : [
			    	{
					"type": "POST",
					"end_point":"/sample/get",
					"post_param": {"key":"value"},
					"query_param": {"key":"value"},
					"headers": {"key":"value"},
			     	},
				{
					"type": "POST",
					"end_point":"/sample/post",
					"post_param": {"key":"value"},
					"query_param": {"key":"value"},
					"headers": {"key":"value"},
					"handler_callback": "follow_get_request"
			     	}
			    ],
		"response" : [
				{
					"http_status": 200,
					"body": {"key":"value"},
					"header": {"key":"value"},
					"handler_callback": "follow_get_response"
			     	},
				{
					"http_status": 200,
					"body": {"key":"value"},
					"header": {"key":"value"},
					"handler_callback": "post_handler"
			     	}
			     ]
		}
	      ]
}
===============================================================================
