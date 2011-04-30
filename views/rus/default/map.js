function(doc)  {
    if(doc.type !== "rus") return;
    
    emit([doc.year, doc.rustur, doc.name], null);
    
}

