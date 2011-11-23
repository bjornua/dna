import sys

import app.tool.help as help_
import app.tool.config_setup as config_setup
import app.tool.update_database as update_database

tools = [
    config_setup,
    help_,
    update_database
]


def main():
    if len(sys.argv) < 2:
        sys.stderr.write(u"You didn't specify a command\n")
        sys.stderr.flush()
        return

    name = sys.argv[1]

    possibletools = [t for t in tools if t._toolname.startswith(name)]
    
    if len(possibletools) > 1:
        sys.stderr.write(u"Ambiguous command %s could be:\n" %(name, ))
        for tool in possibletools:
            sys.stderr.write(u"* %s\n" % (tool._toolname,))
        sys.stderr.flush()
        return

    if len(possibletools) < 1:
        sys.stderr.write("Could't find command %s\n" % (name,))
        sys.stderr.flush()
        return

    tool, = possibletools
    
    tool.main()
        

if __name__ == "__main__":
    main()
