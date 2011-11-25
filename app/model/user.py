# -*- coding: utf-8 -*-
from app.utils.misc import db, local
from random import choice
from couchdbkit import ResourceNotFound


import app.utils.iptables as iptables
import app.utils.arp as arp
import app.config

config = app.config.get()

class UserExist(Exception): pass
class UserDoesntExist(Exception): pass

def generatepassword(chars="ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnpqrstuvwxyz23456789", length=10):
    return "".join(choice(chars) for x in range(length))

def get(uid):
    try:
        doc = db()[uid]
    except ResourceNotFound:
        raise UserDoesntExist("The user with id %s was not found" % (repr(uid),))

    if doc.get("type") != "user":
        raise UserDoesntExist("Document id %s is not a user" % (repr(uid),))

    return doc


def authenticate(username, password):
    for x in db().view("user/auth", key=[username, password], include_docs=True):
        doc = x["doc"]
        break
        
    macs = doc["macaddrs"]
    maxmacs = doc["macaddrs_max"]
    
    macaddr = "00:1e:64:7d:ed:78"

    if macaddr != None:
        macs.append(macaddr)

        while len(macs) > maxmacs:
            iptables.delmac(macs.pop(0))
        
        if len(macs) == 0:
            return

        iptables.addmac(macaddr)
        
        db().save_doc(doc)
        
        return x["id"]


def create(username, email, macaddrs_max, password=u""):
    if password == u"":
        password = generatepassword()
    
    userid = getid(username)
    if userid != None:
        raise UserExist("User %s already exist with id %s" % (repr(username), repr(userid)))

    db().save_doc({
        "type": "user",
        "username": username,
        "email": email,
        "macaddrs_max": macaddrs_max,
        "macaddrs": [],
        "password": password,
    })

def update(uid, username=None, email=None, macaddrs_max=None, password=None):
    doc = get(uid)
    
    if username != None:
        if username != doc["username"]:
            userid = getid(username)
            if userid != None:
                raise UserExist("User %s already exist with id %s" % (repr(username), repr(userid)))
            
        doc["username"] = username

    if email != None:
        doc["email"] = email

    if macaddrs_max != None:
        doc["macaddrs_max"] = macaddrs_max
    
    if password != None:
        doc["password"] = password
    
    db().save_doc(doc)

def delete(uid):
    get(uid) # Make sure the user exist and display pretty error message if not
    db().delete_doc(uid)

def getid(username):
    for x in db().view("user/auth", startkey=[username, u""], endkey=[username, u"\ufff0"], limit=1):
        return x["id"]

def getmacs():
    for x in db().view("user/macaddr"):
        yield x["key"][0]


def getname(uid):
    return db()[uid]["username"]

def list_docs():
    for x in db().view("user/auth", include_docs=True):
        yield x["doc"]
