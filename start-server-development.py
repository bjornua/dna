#!/usr/bin/python2 -B
# -*- coding: utf-8 -*-
import env

from werkzeug import run_simple
from app.application import Application

app = Application(debug=True)
bind_address = "0.0.0.0"
port = 5000
run_simple(
    bind_address, port, app, use_debugger=True, use_reloader=True
)
