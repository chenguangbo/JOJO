from wsgiref.simple_server import make_server
def app(environ, start_respponse):
    status = "200 OK"
    header = [('Content-type', 'text/html')]
    start_respponse(status, header)

    return 'Hello World'.encode('utf-8')


httpd = make_server('127.0.0.1', 8080, app)
print("Sever on port 8080.....")
httpd.serve_forever()