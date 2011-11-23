from app.utils.misc import template_response, local, db, urlfor, redirect

def index():
    template_response("/page/router/index.mako")

