# -*- coding: utf-8 -*-
from app.utils.misc import template_response, local, db, urlfor, redirect, authcheck

def index():
    if not authcheck():
        return


    template_response("/page/router/index.mako")

