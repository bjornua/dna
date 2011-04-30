# -*- coding: utf-8 -*-
import werkzeug.routing

import app.controllers.index
import app.controllers.router
import app.controllers.lan
import app.controllers.error

endpoints = {
    "index": app.controllers.index.index,
    "routing.index": app.controllers.router.index,
    "routing.close": app.controllers.error.notyet,
    "routing.open": app.controllers.error.notyet,
    "firewall.index": app.controllers.error.notyet,
    "lan.index": app.controllers.lan.index,
    "wan.index": app.controllers.error.notyet,
    "user.index": app.controllers.error.notyet,
    "notfound": app.controllers.error.notfound,
    "error": app.controllers.error.error
}

url_map = werkzeug.routing.Map()

for method, path, endpoint in [
        ("GET", "/", "index"),
        ("GET", "/routing", "routing.index"),
        ("GET", "/routing/open", "routing.open"),
        ("GET", "/routing/close", "routing.close"),
        ("GET", "/lan", "lan.index"),
        ("GET", "/wan", "wan.index"),
        ("GET", "/firewall", "firewall.index"),
        ("GET", "/users", "user.index"),
    ]:
    rule = werkzeug.routing.Rule(path, methods=[method], endpoint=endpoint)
    url_map.add(rule)
