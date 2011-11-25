#!/usr/bin/python2
# -*- coding: utf-8 -*-
import env
import wsgiserver

from app.application import Application

app = Application(debug=False)
bind_address = "0.0.0.0"
port = 5000

server = wsgiserver.CherryPyWSGIServer((bind_address, port), app)

server.start()
