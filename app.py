from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.stack_context import NullContext
from tornado.wsgi import WSGIContainer
# from MirisHuesWebapp import app
from os import environ

from flask import Flask

app = Flask(__name__)

wsgi_app = app.wsgi_app

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT, debug=True)

    # http_server = HTTPServer(WSGIContainer(app))
    # with NullContext():
    #     http_server.bind(port=5555, address="127.0.0.1")
    #     http_server.start(6)
    # IOLoop.instance().start()
