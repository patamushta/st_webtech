

def wsgi_app(environ, start_response):
    status = '200 OK'
    headers = [
            ('Content-Type', 'text/plain')
#            ('Content-Type', 'text/html')
    ]
    parameters = environ.get('QUERY_STRING', '')
    body = parameters.replace("&", "\n")
    start_response(status, headers)
    return [ body ] 

# test usage
#if __name__ == '__main__':
#    from wsgiref.simple_server import make_server
#    srv = make_server(
#            'localhost', 8080,
#            wsgi_app)
#    srv.serve_forever()
