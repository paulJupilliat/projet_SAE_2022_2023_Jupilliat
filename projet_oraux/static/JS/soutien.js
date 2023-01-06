
function changeColor(e){
    var val = e.value;
    if (val.split(" ")[0] == "dispo")
    {
        e.style.backgroundColor = "#9afa7d";
    }
    else
    {
        if (val !="-"){
        e.style.backgroundColor = "#fae77d";}
        else{
            e.style.backgroundColor = "white";
        }
    }

};