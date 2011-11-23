# -*- coding: utf-8 -*-
from os.path import join

from werkzeug import Request, Response, SharedDataMiddleware
from werkzeug.exceptions import NotFound

from app.mapping import url_map, endpoints
from app.utils.misc import local, path
from app.utils.session import Session

class Application(object):
    def __init__(self, debug):
        local.application = self
        self.debug = debug
        self.dispatch = SharedDataMiddleware(self.dispatch, {"/static": path["static"]})
    
    def dispatch(self, environ, start_response):
        try:
            local.request = Request(environ)
            local.response = Response()
            local.session = Session(local.request.cookies.get("session"), 600)
            try:
                local.url_adapter = url_adapter = url_map.bind_to_environ(environ)
                try:
                    endpoint, params = url_adapter.match()
                except NotFound:
                    endpoint = "notfound"
                    params = {}
                local.endpoint = endpoint
                endpoints[endpoint](**params)
            except:
                if self.debug:
                    raise
                endpoints["error"]()
            response = local.response
            local.session.save()
            local.session.set_cookie(local.response)
        except: 
            if self.debug:
                raise
            response = Response("Fejlsidens fejlside.")
            
        return response(environ, start_response)        
    def __call__(self, environ, start_response):
        local.application = self
        return self.dispatch(environ, start_response)
