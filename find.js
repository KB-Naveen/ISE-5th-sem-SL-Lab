function find(){
    var s = document.getElementById("text").value
    var l = s.split(" ")
    var w;
    var n=0;
    
    for(i=0;i<l.length;i++){
        if(l[i].length>n){
            n = l[i].length
            w = l[i]
        }
    }

    document.getElementById("res").innerHTML = "Longest word : "+w+" , Word Length : "+n
}