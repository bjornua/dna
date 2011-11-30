# -*- coding: utf-8 -*-
import threading
import time
import subprocess
import app.utils.date as dateutils

from app.utils.misc import db

def runinterval(interval=1):
    def decorator(f):
        def job(*args, **kwargs):
            while True:
                threading.Thread(target=f, args=args, kwargs=kwargs).start()
                time.sleep(interval)
        return job
    return decorator

@runinterval(1)
def collect_mactraffic():
    args = [
        "/usr/sbin/iptables",
        "-t", "mangle",
        "--list-rules", "maclist",
        "--zero", "--verbose"
    ]
    
    date = dateutils.nowtuple()
    for line in subprocess.check_output(args).split("\n"):
        line = line.strip()
        
        if len(line) == 0:
            continue

        columns = line.split(" ")
        
        try:
            imac = columns.index("--mac-source")
            itraffic = columns.index("-c")
        except ValueError:
            continue

        mac = columns[imac+1]
        packetcount, bytecount = map(int, columns[itraffic+1:itraffic+3])
        print repr((date, mac, packetcount, bytecount))
