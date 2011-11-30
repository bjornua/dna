#!/usr/bin/python2
# -*- coding: utf-8 -*-
import env
import time
import wsgiserver

from app.application import Main, Redirecter
from threading import Thread


webapp = Main(debug=False)
redirecter = Redirecter(debug=False)

bind_address = "0.0.0.0"
redirecter_port = 80
app_port = 5000

webapp = wsgiserver.CherryPyWSGIServer((bind_address, app_port), webapp)
redirecter = wsgiserver.CherryPyWSGIServer((bind_address, redirecter_port), redirecter)

for target in (webapp, redirecter):
    t = Thread(target=target.start)
    t.daemon = True
    t.start()

try:
    while True:
        time.sleep(999)
except KeyboardInterrupt:
    webapp.stop()
    redirecter.stop()

