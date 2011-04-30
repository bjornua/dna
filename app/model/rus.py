from app.utils.misc import db

from pprint import pprint

def browse_total_pages(perpage=10):
    result = db().view("rus/default", reduce=True)
    for row in result:
        return ((row.value - 1) // perpage) + 1

def browse(page=0, perpage=10):
    skip = page * perpage
    result = db().view("rus/default", include_docs=True, skip=skip, limit=perpage, reduce=False)
    
    for row in result:
        doc = row.doc
        
        name = doc.get("name")
        phone = doc.get("phone")
        email = doc.get("email")
        year = doc.get("year")
        rustur = doc.get("rustur")
        
        id = doc.id
        name = name and unicode(name)
        phone = phone and unicode(phone)
        email = email and unicode(email)
        rustur = rustur and unicode(rustur)

        if year != None:
            year = unicode(year)
        
        yield id, name, phone, email, year, rustur


def info(id):
    doc = db()[id]

    name = doc.get("name")
    phone = doc.get("phone")
    email = doc.get("email")
    year = doc.get("year")
    rustur = doc.get("rustur")
    
    id = doc.id
    name = name and unicode(name)
    phone = phone and unicode(phone)
    email = email and unicode(email)
    year = year and unicode(year)
    rustur = rustur and unicode(rustur)

    return name, phone, email, year, rustur

def update(id, name, phone, email, year, rustur):
    doc = db()[id]

    for fieldname, fieldvalue in (
        ("name", name),
        ("phone", phone),
        ("email", email),
        ("year", year),
        ("rustur", rustur),
    ):
        if fieldvalue == None and fieldname in doc:
            del doc[fieldname]
        else:
            doc[fieldname] = fieldvalue
    db().save(doc)
