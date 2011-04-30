# -*- coding: utf-8 -*-
import json
import os.path
import xml.sax.saxutils

import couchdb
import werkzeug
import werkzeug.routing
import werkzeug.utils
import mako.lookup

import app.widget
from app.config.generated import config

path = {}
path["root"] = os.path.join(os.path.dirname(__file__), "..")
path["static"] = os.path.join(path["root"], "../static")
path["templates"] = os.path.join(path["root"], "../templates")

local = werkzeug.Local()
local_manager = werkzeug.LocalManager([local])
application = local("application")

def db():
    return couchdb.Server(config["couchdb_server_url"])[config["couchdb_db"]]

template_lookup = mako.lookup.TemplateLookup(
    directories=[path["templates"]],
    input_encoding="utf-8",
    output_encoding="utf-8"
)

def url_for(endpoint, method=None, _external=False, **values):
    return local.url_adapter.build(endpoint, values, method=method, force_external=_external)

si_units = (
    ("deca", 1e1),
    ("hecto", 1e2),
    ("kilo", 1e3),
    ("mega", 1e6),
    ("giga", 1e9),
    ("tera", 1e12),
    ("peta", 1e15),
    ("exa" , 1e18),
    ("zetta", 1e21),
    ("yotta", 1e24)
)

def format_size(number):
    prev = si_units[0]
    
    if number < prev[1]:
        return "%i bytes" % (number,)

    for x in si_units[1:]:
        if number < x[1]:
            break
        prev = x
         
    number /= prev[1]

    return "%.1f %sbytes" % (number, prev[0])

def template_response(templatename, **kwargs):
    kwargs["response"] = local.response
    local.response.data = template_render(templatename, **kwargs)

def template_render(templatename, **kwargs):
    template = template_lookup.get_template(templatename)
    kwargs.update({
        "format_size": format_size,
        "url_for": url_for,
        "esc_attr": xml.sax.saxutils.quoteattr,
        "escape": xml.sax.saxutils.escape,
        "json": json.dumps,
        "endpoint": local.endpoint,
        "endpoint_override": None,
        "widget": app.widget
    })
    return template.render(**kwargs).decode("utf-8")

def redirect(endpoint, *args, **kwargs):
    local.response = werkzeug.utils.redirect(url_for(endpoint, *args, **kwargs))
