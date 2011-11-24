# -*- coding: utf-8 -*-
import app.model.user as user
import app.config
import app.utils.arp
import app.utils.iptables
import werkzeug.utils
from app.utils.misc import template_response, local, db, urlfor, redirect, debug
from app.controllers.error import notfound

config = app.config.get()

def login_form():
    error = local.request.args.get("error")
    error = error != None
    template_response("/netlogon.mako",
        error = error
    )

def login_do():
    username = local.request.form.get("username")
    password = local.request.form.get("password")

    uid = user.authenticate(username, password)

    if uid == None:
        redirect("netlogon.login_form", error="")
        return

    macaddr = app.utils.arp.arping(config["interface_lan"], local.request.remote_addr)
    
    if macaddr != None:
        app.utils.iptables.addmac(macaddr)

    local.response = werkzeug.utils.redirect("http://www.dikulan.dk/", 307)
