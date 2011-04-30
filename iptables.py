# iptables interface
import subprocess
import threading

def run(args):
    args = ["/bin/echo"] + args
    process = subprocess.Popen(args)
    process.wait()

iptables_lock = threading.RLock()
def run_iptables(args):
    with iptables_lock:
        run(["/usr/sbin/iptables"] + args)


run_iptables(["herp", "derp"])

