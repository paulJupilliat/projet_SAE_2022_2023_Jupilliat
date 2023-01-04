function plie_deplie_matieres() {
    const img = document.getElementById("dep");
    if (document.getElementById("matieres_gauche").style.display == "none") {
        document.getElementById("matieres_gauche").style.display = "block";
    } else {
        document.getElementById("matieres_gauche").style.display = "none";
    }
    if (img.src.match("../img/plie.png")) {
        img.src = "../img/deplie.png";
    } else {
        img.src = "../img/plie.png";
    }
};
function collapse(){
    // this.classList.toggle("active");
    var content = document.getElementById("content");
    var bt=document.getElementById("collapsible");
    if (content.style.display === "block") {
        content.style.display = "none";
        bt.innerHTML='<img src="static/img/plus.png" alt="+" height="10em">'
    } else {
        content.style.display = "block";
        bt.innerHTML='<img src="static/img/moins.png" alt="-" height="10em">'
    }
  };
