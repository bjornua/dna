#!/usr/bin/python2 -B
# -*- coding: utf-8 -*-
import env

from werkzeug import run_simple
from app.application import Application

app = Application(debug=True)
bind_address = "127.0.0.1"
port = 5000
run_simple(
    bind_address, port, app, use_debugger=True, use_reloader=True
)
