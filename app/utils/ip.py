# -*- coding: utf-8 -*-
import subprocess

def getip(interface):
    args = ["/sbin/ip", "addr", "show", "dev", interface]
    process = subprocess.Popen(args, stdout=subprocess.PIPE)
    process.wait()

    out = process.stdout.read()
    out = [x.strip().split(" ") for x in out.split("\n")]
    return [x[1].split("/")[0] for x in out if x[0] == "inet"][0]
