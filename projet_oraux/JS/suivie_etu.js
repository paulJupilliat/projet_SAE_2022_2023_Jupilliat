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

