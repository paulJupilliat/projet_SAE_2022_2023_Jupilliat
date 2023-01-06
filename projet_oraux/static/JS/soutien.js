
function changeColor(e){
    var val = e.value;
    console.log(val);
    if (val.split(" ")[0] == "dispo")
    {
        e.style.backgroundColor = "green";
    }
    else
    {
        e.style.backgroundColor = "yellow";
    }

};