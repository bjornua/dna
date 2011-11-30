# -*- coding: utf-8 -*-
from os.path import join

from werkzeug import Request, Response, SharedDataMiddleware
from werkzeug.exceptions import NotFound

from app.mapping import url_map, endpoints
from app.utils.misc import local, path
from app.utils.session import Session

import app.config
import app.model.user as user
import app.utils.iptables as iptables
import app.logger

logger = app.logger.get(__name__)
config = app.config.get()

class Application(object):
    def __init__(self, debug):
        local.application = self
        iptables.reset(config["interface_lan"], config["interface_wan"])
        for addr in user.getmacs():
            iptables.addmac(addr)
        self.debug = debug
        self.dispatch = SharedDataMiddleware(self.safedispatch, {"/static": path["static"]})
    
    def safedispatch(self, environ, start_response):
        try:
            return self.appdispatch(environ, start_response)
        except: 
            if self.debug:
                raise
            logger.exception("Exception")
            return Response("Fejlsidens fejlside.")(environ, start_response)

    def appdispatch(self, environ, start_response):
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
            else:
                logger.exception("Exception")
                endpoints["error"]()
        response = local.response
        local.session.save()
        local.session.set_cookie(local.response)
            
        return response(environ, start_response)
    def __call__(self, environ, start_response):
        local.application = self
        return self.dispatch(environ, start_response)
