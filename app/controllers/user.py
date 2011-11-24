# -*- coding: utf-8 -*-
from app.utils.misc import template_response, local, db, urlfor, redirect, debug
from app.controllers.error import notfound

import app.model.user as user


def list():
    users = ((
        doc["_id"],
        doc["username"],
        doc["email"],
        doc["macaddrs"]
        ) for doc in user.list_docs())
    template_response("/page/user/list.mako",
        users=users
    )

def edit_form(uid):
    try:
        doc = user.get(uid)
    except user.UserDoesntExist:
        notfound()
        return
    
    args = local.request.args
    errors = set(filter(len, args.get(u"errors", "").split(u",")))
    username = args.get(u"username", doc["username"])
    email = args.get(u"email", doc["email"])
    macaddrs_max = args.get(u"macaddrs_max", doc["macaddrs_max"])
    

    template_response("/page/user/edit.mako", 
        uid=uid,
        username=username,
        email=email,
        macaddrs_max=macaddrs_max,
        errors=errors
    )

def edit_do(uid):
    form = local.request.form
    username = form.get("username")
    email = form.get("email")
    macaddrs_max = form.get("macaddrs_max")
    password0 = form.get("password0")
    password1 = form.get("password1")
    
    errors = set()
    if password0 != password1:
        errors.add("passwordmatch")

    try:
        macaddrs_max = int(macaddrs_max)
    except ValueError:
        errors.add("macaddrs_max_type")
    else:
        if not macaddrs_max >= 0:
            errors.add("macaddrs_max_range")
    if len(errors) > 0:
        redirect("user.edit_form", uid=uid, errors=",".join(errors), username=username, email=email, macaddrs_max=macaddrs_max)
        return
    
    if len(password0)==0:
        password0 = None

    user.update(uid, username=username, email=email, macaddrs_max=macaddrs_max, password=password0)
    redirect("user.list")

def create_form():
    args = local.request.args
    
    errors = set(filter(len, args.get(u"errors", "").split(u",")))
    username = args.get(u"username", u"")
    email = args.get(u"email", u"")
    macaddrs_max = args.get(u"macaddrs_max", u"1")
    


    template_response("/page/user/create.mako", 
        username=username,
        email=email,
        macaddrs_max=macaddrs_max,
        errors=errors
    )

def create_do():
    form = local.request.form
    username = form.get("username")
    email = form.get("email")
    macaddrs_max = form.get("macaddrs_max")
    password0 = form.get("password0")
    password1 = form.get("password1")
    
    errors = set()
    if password0 != password1:
        errors.add("passwordmatch")

    try:
        macaddrs_max = int(macaddrs_max)
    except ValueError:
        errors.add("macaddrs_max_type")
    else:
        if not macaddrs_max >= 0:
            errors.add("macaddrs_max_range")
    if len(errors) > 0:
        redirect("user.create_form", errors=",".join(errors), username=username, email=email, macaddrs_max=macaddrs_max)
        return
    
    user.create(username=username, email=email, macaddrs_max=macaddrs_max, password=password0)
    redirect("user.list")

def delete(uid):
    user.delete(uid)
    redirect("user.list")
