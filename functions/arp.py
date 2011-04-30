import subprocess
import re

def arpcachedict():
    arptable = open("/proc/net/arp").read()
    arptable = arptable.split("\n")
    arptable = arptable[1:-1]
    arptable = (x.split(" ")   for x in arptable)
    arptable = (filter(len, x) for x in arptable)
    arptable = (((x[5], x[0]), x[3])   for x in arptable)
    return dict(arptable)

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

