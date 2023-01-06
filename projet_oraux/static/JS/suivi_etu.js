function plie_deplie_matieres() {
    const img = document.getElementById("dep");
    if (document.getElementById("matieres_gauche").style.display == "none") {
        document.getElementById("matieres_gauche").style.display = "flex";
    } else {
        document.getElementById("matieres_gauche").style.display = "none";
    }
    if (img.src.match("./static/img/plie.png")) {
        img.src = "./static/img/deplie.png";
    } else {
        img.src = "./static/img/plie.png";
    }
};
function collapse(){
    // this.classList.toggle("active");
    var content = document.getElementById("content");
    var bt=document.getElementById("collapsible");
    if (content.style.display === "flex") {
        content.style.display = "none";
        bt.innerHTML='+'
    } else {
        content.style.display = "flex";
        bt.innerHTML='-'
    }
  };
