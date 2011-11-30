# -*- coding: utf-8 -*-
import subprocess
import threading
import app.utils.ip

def run(args):
    args = args
    print args
    process = subprocess.Popen(args)
    process.wait()

iptables_lock = threading.RLock()
def iptables(args):
    global iptables_lock

    with iptables_lock:
        run(["/usr/sbin/iptables"] + args)

def reset(interface_lan, interface_wan):
    global iptables_lock
    with iptables_lock:
        # HACK: In case there are links (dependencies), run three times (one for each table)
        # DISCLAIMER: This is not not very considered, and might be an arbitrary thing to do
        for x in range(3):
            iptables(["-t", "filter", "-X"])
            iptables(["-t", "filter", "-F"])
            iptables(["-t", "mangle", "-X"])
            iptables(["-t", "mangle", "-F"])
            iptables(["-t", "nat"   , "-X"])
            iptables(["-t", "nat"   , "-F"])
        

        iptables(["-t", "filter", "-P", "INPUT"  , "DROP"])
        iptables(["-t", "filter", "-P", "FORWARD", "DROP"])
        iptables(["-t", "mangle", "-N", "maclist"])
        iptables(["-t", "mangle", "-A", "PREROUTING", "-j", "maclist"])

        # Allow established traffic to this computer
        iptables(["-t", "filter", "-A", "INPUT", "-m", "state", "--state", "ESTABLISHED,RELATED", "-j", "ACCEPT"])
        
        for proto, port in (
            ("tcp", 22),
            ("tcp", 80),
            ("tcp", 5000),
            ("udp", 5353),
        ):
            iptables(["-t", "filter", "-A", "INPUT", "-p", proto, "-i", interface_lan, "--dport", str(port), "-j", "ACCEPT"])

        # Allow loopback traffic
        iptables(["-t", "filter", "-A", "INPUT", "-i", "lo", "-j", "ACCEPT"])

        # Allow established traffic regardless of source interface
        iptables(["-t", "filter", "-A", "FORWARD", "-m", "state", "--state", "ESTABLISHED,RELATED", "-j", "ACCEPT"])
        
        # Allow authenticated MAC addresses (packets marked decimal 99) to initiate traffic
        iptables(["-t", "filter", "-A", "FORWARD", "-i", interface_lan, "-o", interface_wan, "-m", "mark", "--mark", "99", "-j", "ACCEPT"])
        
        iptables(["-t", "filter", "-A", "FORWARD", "-i", interface_lan, "-p", "udp", "--dport", "53", "-j", "ACCEPT"])
        iptables(["-t", "filter", "-A", "FORWARD", "-i", interface_lan, "-p", "tcp", "--dport", "53", "-j", "ACCEPT"])
        iptables(["-t", "filter", "-A", "FORWARD", "-i", interface_lan, "-p", "udp", "--dport", "53", "-j", "ACCEPT"])
        
        iptables(["-t", "nat", "-A", "PREROUTING" , "-m", "mark", "!", "--mark", "99", "-p", "tcp", "--dport", "80", "-j", "DNAT", "--to-destination", app.utils.ip.getip(interface_lan)])
        iptables(["-t", "nat", "-A", "POSTROUTING", "-o", interface_wan, "-j", "MASQUERADE"])
        
        # End of table. Since this is allow/deny, send reject packets now
        iptables(["-A", "INPUT"  , "-j", "REJECT"])
        iptables(["-A", "FORWARD", "-j", "REJECT"])

    # Enable packet forwarding if not already enabled
    with open("/proc/sys/net/ipv4/ip_forward", "w") as f:
        print >> f, 1

def addmac(macaddr):
    iptables(["-t", "mangle", "-A", "maclist", "-m", "mac", "--mac-source", macaddr, "-j", "MARK", "--set-mark", "99"])

def delmac(macaddr):
    iptables(["-t", "mangle", "-D", "maclist", "-m", "mac", "--mac-source", macaddr, "-j", "MARK", "--set-mark", "99"])

