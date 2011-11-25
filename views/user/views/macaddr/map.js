function(doc) {
    if(doc.type !== "user") return;
    
    doc.macaddrs.forEach(function(addr){
        emit([addr], null);
    });
}
