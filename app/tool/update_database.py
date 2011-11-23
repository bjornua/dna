# -*- coding: utf-8 -*-
_toolname = "push_views"
_tooldesc = "Pushes whatever CouchDB javascript views it can find in ./views"

import couchdbkit
from app.utils.misc import db
from app.utils.folder import get_nodes
import os.path as path

def main():
    views = set()
    for p in get_nodes(["views"]):
        if len(p) != 2:
            continue
        
        p = path.join(*p)

        if not path.isdir(p):
            continue
        
        couchdbkit.designer.push(p, db())
