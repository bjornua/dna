#!/usr/bin/python2
# -*- coding: utf-8 -*-
import app.config
import env
import time
import wsgiserver

from app.application import Application
from app.utils.ip import getip
from threading import Thread

config = app.config.get()

webapp = Application(debug=False)
lan_ip = getip(config["interface_lan"])

bind_address = "0.0.0.0"
redirecter_port = 4000
app_port = 5000

webapp = wsgiserver.CherryPyWSGIServer((bind_address, app_port), webapp)
def redirecter(env, start_r):
        start_r('307 Temporary Redirect', [('Location', 'http://' + lan_ip + ":5000/")])
        return []

redirecter = wsgiserver.CherryPyWSGIServer((bind_address, redirecter_port), redirecter)

Thread(target=webapp.start).start()
Thread(target=redirecter.start).start()

try:
    while True:
        time.sleep(999)
except KeyboardInterrupt:
    webapp.stop()
    redirecter.stop()

