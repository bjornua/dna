#!/usr/bin/python2
# -*- coding: utf-8 -*-
import env
import wsgiserver
import app.config
from app.application import Application
from app.utils.ip import getip
config = app.config.get()

lan_ip = getip(config["interface_lan"])

bind_address = "0.0.0.0"
port = 80
   

def app(env, start_r):
        start_r('307 Temporary Redirect', [('Location', 'http://' + lan_ip + ":5000/")])
        return []

server = wsgiserver.CherryPyWSGIServer((bind_address, port), app)

server.start()
