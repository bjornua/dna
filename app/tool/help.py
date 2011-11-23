# -*- coding: utf-8 -*-
import sys

_toolname = u"help"
_tooldesc = u"This command :P"

def main():
    import app.tool.main as main_
    if len(sys.argv) < 3:
        name = ""
    else:
        name = sys.argv[2]

    toolsfound = 0
    for t in main_.tools:
        if not t._toolname.startswith(name):
            continue
        toolsfound += 1

        print "* %s - %s" % (t._toolname, t._tooldesc)

    if toolsfound == 0:
        sys.stderr.write("Command(s) not found\n")
        sys.stderr.flush()
        
    
