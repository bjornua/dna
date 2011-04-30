function(doc) {
    if(doc.type !== "doc") return;
    if(doc.tags === undefined) return;
    
    
    // Sort the tags
    tags = doc.tags.slice();
    
    tags.sort();
    
    // Remove duplicates
    result = [];
    if(tags.length !== 0){
        result.push(tags[0]);
    }
    
    for(i=1; i<tags.length; i++){
        if(tags[i-1] !== tags[i]){
            result.push(tags[i]);
        }
    }
    
    tags = result;
    
    if(tags.length > 8){
        return;
    }
    
    function rotate(size){
        if(size < 3){
            if(size == 2){
                return [[1],[0,1]];
            }
            if(size == 1){
                return [[0]];
            }
            return [];
        }
        a = [[size-1]];
        result = new Array();
        while(a.length !== 0){
            b = new Array();
            for(i=0; i<a.length; i++){
                for(j=1; j<a[i][0]; j++){
                    b.push([j].concat(a[i]));
                    result.push([j].concat(a[i]));
                }
                result.push([0].concat(a[i]));
            }
            a = b;
        }
        return result;
    }
    rotate(tags.length).forEach(function(x){
        emit(x.map(function(i){ return tags[i]; }), null);
    });
}
