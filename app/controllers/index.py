# -*- coding: utf-8 -*-
from app.utils.misc import template_response, local, db, urlfor, redirect, adminauth, authcheck

def index():
    if not authcheck():
        return
    template_response("/page/index.mako")

def login_form():
    template_response("/page/adminlogin.mako")

def login_do():
    password = local.request.form.get("password", u"")
    
    if adminauth(password):
        local.session["authed"] = True
        redirect("index")
        return

    redirect("admin.login_form")
    return

def logout():
    if not authcheck():
        return
    local.session["authed"] = False
    redirect("admin.login_form")
