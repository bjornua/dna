from app.utils.misc import template_response, local, db, url_for, redirect

def index():
    template_response("/page/router/index.mako")

