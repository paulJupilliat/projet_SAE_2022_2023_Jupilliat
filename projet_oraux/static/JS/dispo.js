function plie_deplie_filtres() {
    const img = document.getElementById("dep");
    if (document.getElementById("grps_filtres").style.display == "none") {
        document.getElementById("grps_filtres").style.display = "block";
    } else {
        document.getElementById("grps_filtres").style.display = "none";
    }
    if (img.src.match("./static/img/plie.png")) {
        img.src = "./static/img/deplie.png";
    } else {
        img.src = "./static/img/plie.png";
    }
};

function plie_deplie_semaines() {
    const img = document.getElementById("dep2");
    if (document.getElementById("groupe_filtre").style.display == "none") {
        document.getElementById("groupe_filtre").style.display = "block";
    } else {
        document.getElementById("groupe_filtre").style.display = "none";
    }
    if (img.src.match("./static/img/plie.png")) {
        img.src = "./static/img/deplie.png";
    } else {
        img.src = "./static/img/plie.png";
    }
};
