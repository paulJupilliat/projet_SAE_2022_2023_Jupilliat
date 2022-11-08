// lorsque le boutton dont l'id est donne est clique on appelle la fonction plie_deplie



function plie_deplie_filtres() {
    const img = document.getElementById("dep");
    if (document.getElementById("grps_filtres").style.display == "none") {
        document.getElementById("grps_filtres").style.display = "block";
    } else {
        document.getElementById("grps_filtres").style.display = "none";
    }
    if (img.src.match("../img/plie.png")) {
        img.src = "../img/deplie.png";
    } else {
        img.src = "../img/plie.png";
    }
};

function plie_deplie_semaines() {
    const img = document.getElementById("dep2");
    if (document.getElementById("groupe_filtre").style.display == "none") {
        document.getElementById("groupe_filtre").style.display = "block";
    } else {
        document.getElementById("groupe_filtre").style.display = "none";
    }
    if (document.getElementById("selec-sem").style.display == "none") {
        document.getElementById("selec-sem").style.display = "block";
    } else {
        document.getElementById("selec-sem").style.display = "none";
    }
    if (img.src.match("../img/plie.png")) {
        img.src = "../img/deplie.png";
    } else {
        img.src = "../img/plie.png";
    }
};
