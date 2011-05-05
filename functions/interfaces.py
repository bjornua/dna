import socket
from fcntl import ioctl
from struct import pack, unpack
import subprocess

SIOCGIFADDR    = 0x8915 # get PA address
SIOCSIFADDR    = 0x8916 # set PA address

SIOCGIFBRDADDR = 0x8919 # get broadcast PA address
SIOCSIFBRDADDR = 0x891a # get broadcast PA address

SIOCGIFNETMASK = 0x891b # get network PA mask
SIOCSIFNETMASK = 0x891c # set network PA mask

SIOCGIFMTU     = 0x8921 # get MTU size
SIOCSIFMTU     = 0x8922 # set MTU size

SIOCGIFHWADDR  = 0x8927 # get hardware address
SIOCSIFHWADDR  = 0x8924 # set hardware address

def getifoptions(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    ioarg = pack("16s240x", ifname)
    
    addrret = ioctl(s, SIOCGIFADDR, ioarg)
    addr = unpack("20x4B232x", addrret)
    
    netmaskret = ioctl(s, SIOCGIFNETMASK, ioarg)
    netmask = unpack("20x4B232x", netmaskret)

    broadcastret = ioctl(s, SIOCGIFBRDADDR, ioarg)
    broadcast = unpack("20x4B232x", broadcastret)
    
    mturet = ioctl(s, SIOCGIFMTU, ioarg)
    mtu, = unpack("16xI236x", mturet)
    
    macaddrret = ioctl(s, SIOCGIFHWADDR, ioarg)
    macaddr = unpack("18x6B232x", macaddrret)
    

    return addr, netmask, broadcast, macaddr, mtu

def setifoptions(ifname, addr=None, netmask=None, broadcast=None, macaddr=None, mtu=None):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    if addr != None:
        addr_packed = pack("16sB3x4B232x", ifname, socket.AF_INET, *addr)
        ioctl(s, SIOCSIFADDR, addr_packed)

    if netmask != None:
        netmask_packed = pack("16sB3x4B232x", ifname, socket.AF_INET, *netmask)
        ioctl(s, SIOCSIFNETMASK, netmask_packed)

    if broadcast != None:
        broadcast_packed = pack("16sB3x4B232x", ifname, socket.AF_INET, *broadcast)
        ioctl(s, SIOCSIFBRDADDR, broadcast_packed)

    if macaddr != None:
        macaddr_packed = pack("16sBx6B232x", ifname, socket.AF_UNIX, *macaddr)
        ioctl(s, SIOCSIFHWADDR, macaddr_packed)
    
    if mtu != None:
        mtu_packed = pack("16sI236x", ifname, mtu)
        ioctl(s, SIOCSIFMTU, mtu_packed)


#setifoptions("eth0", *getifoptions("eth0"))

setifoptions("eth0", addr=(10,0,72,200), netmask=(255,255,255,0))


#herp = getifoptions("lo")
#derp = getifoptions("eth0")
#
#print "\tlo\teth0"
#for x in range(len(herp)):
#    print "%s\t%s\t%s" % (repr(x), repr(herp[x]), repr(derp[x]))



#addrret = ioctl(s, SIOCGIFADDR, ioarg)





#print addr


