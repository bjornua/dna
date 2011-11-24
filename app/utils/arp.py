# -*- coding: utf-8 -*-
import subprocess
import re

reply_re = re.compile(r"\nUnicast reply from .*\[(([0-9A-F]{2}:){5}[0-9A-F]{2})\]")
def arping(iface, addr):
    args = ["arping"]
    args += ["-f"]         # Quit after first reply
    args += ["-w", "2"]    # Quit if not resolved in 2 seconds
    args += ["-I", iface]
    args += [addr] 
    process = subprocess.Popen(args, stdout=subprocess.PIPE)
    process.wait()
    out = process.stdout.read()
    
    result = reply_re.search(out)

    if result != None:
        return result.group(1).lower()
