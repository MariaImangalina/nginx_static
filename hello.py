pythonpath = '/home/box/web/hello.py'
bind = "0.0.0.0:8080"
workers = 4


def application(environ, start_response):
	status = '200 OK'
	headers = [('Content-Type', 'text/plain')]
	body = [bytes(i + '\n', 'ascii') for i in environ['QUERY_STRING'].split('&')]
	start_response(status, headers)
	return body
