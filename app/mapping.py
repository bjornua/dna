# -*- coding: utf-8 -*-
import werkzeug.routing

import app.controllers.index
import app.controllers.router
import app.controllers.lan
import app.controllers.error
import app.controllers.user
import app.controllers.netlogon

endpoints = {
    "index": app.controllers.index.index,
    "routing.index": app.controllers.router.index,
    "routing.close": app.controllers.error.notyet,
    "routing.open": app.controllers.error.notyet,
    "firewall.index": app.controllers.error.notyet,
    "lan.index": app.controllers.lan.index,
    "wan.index": app.controllers.error.notyet,
    "user.list": app.controllers.user.list,
    "user.create_form": app.controllers.user.create_form,
    "user.create_do": app.controllers.user.create_do,
    "user.edit_form": app.controllers.user.edit_form,
    "user.edit_do": app.controllers.user.edit_do,
    "user.delete": app.controllers.user.delete,
    "netlogon.login_form": app.controllers.netlogon.login_form,
    "netlogon.login_do": app.controllers.netlogon.login_do,
    "notfound": app.controllers.error.notfound,
    "error": app.controllers.error.error
}

url_map = werkzeug.routing.Map()

for method, path, endpoint in [
        ("GET", "/", "netlogon.login_form"),
        ("POST", "/", "netlogon.login_do"),
        ("GET", "/admin", "index"),
        ("GET", "/admin/routing", "routing.index"),
        ("GET", "/admin/routing/open", "routing.open"),
        ("GET", "/admin/routing/close", "routing.close"),
        ("GET", "/admin/lan", "lan.index"),
        ("GET", "/admin/wan", "wan.index"),
        ("GET", "/admin/firewall", "firewall.index"),
        ("GET", "/admin/user", "user.list"),
        ("GET", "/admin/user/create", "user.create_form"),
        ("POST", "/admin/user/create", "user.create_do"),
        ("GET", "/admin/user/delete/<string:uid>", "user.delete"),
        ("GET", "/admin/user/edit/<string:uid>", "user.edit_form"),
        ("POST", "/admin/user/edit/<string:uid>", "user.edit_do"),
    ]:
    rule = werkzeug.routing.Rule(path, methods=[method], endpoint=endpoint)
    url_map.add(rule)
