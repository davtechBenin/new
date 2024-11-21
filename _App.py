#Coding:utf-8
import os
import redis
from werkzeug.wrappers import Request, Response
from werkzeug.middleware.shared_data import SharedDataMiddleware

from App import App

class Shortly(object):

    def __init__(self, config):
        self.redis = redis.Redis(
            config['redis_host'], config['redis_port'],
            decode_responses=True)

    def dispatch_request(self, request):
        Obj = App()
        Resp_obj = Response(Obj.Run_execution(request),
            mimetype='text/html')
        for tup in Obj.Get_cookies():
            name,val = tup
            Resp_obj.set_cookie(name,val)
        return Resp_obj

    def wsgi_app(self, environ, start_response):
        response = self.dispatch_request(environ)
        return response(environ, start_response)

    def __call__(self, environ, start_response):
        return self.wsgi_app(environ, start_response)

def create_app(redis_host='localhost', redis_port=6379,with_static=True):
    app = Shortly({
        'redis_host':       redis_host,
        'redis_port':       redis_port
    })
    if with_static:
        app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {
            '/static':  os.path.join(os.path.dirname(__file__), 'static')
        })
    return app

if __name__ == '__main__':
    from werkzeug.serving import run_simple
    app = create_app()
    run_simple('127.0.0.1', 5000, app, use_debugger=True, use_reloader=True)
