function calc(tag) {
    var a = document.getElementById("one").value;
    var b = document.getElementById("two").value;
    var op = tag.getAttribute("id");
    var res = document.getElementById("res");

    if(a=='' || b=='')
        alert("Enter both the operands first");
    else{
        if(op=='add')
            res.innerHTML = "Result : "+(Number(a)+Number(b));
        else if(op=='sub')
            res.innerHTML = "Result : "+(a-b);
        else if(op=='mul')
            res.innerHTML = "Result : "+(a*b)
        else{
            if(b==0){
                alert("Divided by zero is not defined !")
                res.innerHTML = "Result : Not Defined"
            }
            else
                res.innerHTML = "Result : "+(a/b);
        }
    }
}