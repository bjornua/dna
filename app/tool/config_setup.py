# -*- coding: utf-8 -*-
_toolname = "config"
_tooldesc = "Interactively generates the project config files."

import os.path
import sys
import grp

def user_query(itemname, converter, defaultrep, default=None):
    while True:
        if default == None:
            answer = raw_input("Indtast %s: " % (itemname,))
        else:
            answer = raw_input("Indtast %s [%s]: " % (itemname, defaultrep(default)))
            if answer == "":
                return default
        try:
            answer = converter(answer)
        except:
            print "Kunne ikke forstå værdien, prøv igen."
            continue
        return answer

def prompt_update_config():
    try:
        from app.config.generated import config
    except ImportError:
        from app.config.default import config
        config = config()

    for name, key, converter, repr_ in [
        ("CouchDB Server URL", "couchdb_server_url", str, str),
        ("CouchDB db", "couchdb_db", str, str),
    ]:
        config[key] = user_query(name, converter, repr_, config[key])
    return config

def write_config(config):
    filename = os.path.join("app", "config", "generated.py")
    fhandle = open(filename, "w")
    fhandle.write(
        "# -*- coding: utf-8 -*-\n"
      + "from app.config.default import config\n"
      + "config = config()\n"
      + "config.update(" + repr(config) + ")"
    )

def main():
    config = prompt_update_config()
    write_config(config)
