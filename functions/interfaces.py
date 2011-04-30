import socket
from fcntl import ioctl
from struct import pack, unpack
import subprocess

SIOCGIFADDR    = 0x8915 # get PA address
SIOCGIFBRDADDR = 0x8919 # get broadcast PA address
SIOCGIFNETMASK = 0x891b # get network PA mask
SIOCGIFMTU     = 0x8921 # get MTU size
SIOCGIFHWADDR  = 0x8927 # get hardware address

def getifoptions(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    fno = s.fileno()
    ioarg = pack("256s", ifname[:15])
    
    addrret = ioctl(fno, SIOCGIFADDR, ioarg)
    addr = unpack("20x4B232x", addrret)
    
    netmaskret = ioctl(fno, SIOCGIFNETMASK, ioarg)
    netmask = unpack("20x4B232x", netmaskret)

    broadcastret = ioctl(fno, SIOCGIFBRDADDR, ioarg)
    broadcast = unpack("20x4B232x", broadcastret)
    
    mturet = ioctl(fno, SIOCGIFMTU, ioarg)
    mtu = unpack("16xI236x", mturet)
    
    
    macaddrret = ioctl(fno, SIOCGIFHWADDR, ioarg)
    macaddr = unpack("18x6B232x", macaddrret)
    
    

    return addr, netmask, broadcast, macaddr, mtu

def setifoptions(ifname, addr=None, netmask=None, mtu=None, broadcast=None, macaddr=None):
    args = ["/bin/echo", "/sbin/ifconfig"]
    args += [ifname]

    if addr != None:
        addr = ".".join(map(str, addr))
        args += ["address", addr]

    if netmask != None:
        netmask = ".".join(map(str, netmask))
        args += ["netmask", netmask]

    if broadcast != None:
        broadcast = ".".join(map(str, broadcast))
        args += ["broadcast", broadcast]
    
    if mtu != None:
        args += ["mtu", str(mtu)]

    if macaddr != None:
        args += ["hw", "ether", macaddr]

    process = subprocess.Popen(args)
    process.wait()

setifoptions("eth0", (10,0,2,1))
