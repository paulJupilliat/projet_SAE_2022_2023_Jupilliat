// si le nav barr est déja ouvert l'image de la roix est afficher sinon c'est l'image du menu
function changeImage() {
    //si le menu est derouler, on le fait devenir transparant et on change l'image en image de menu
    if(document.getElementById("navbar_menu").style.display == "block"){
        console.log("feur");
        document.getElementById("navbar_menu").style.display = "none";
        document.getElementById("menu").src = "../img/salade_tomate_onion.png";
    }
    else{
        if (document.getElementById("navbar_menu").style.display == "none"){
            document.getElementById("navbar_menu").style.display = "block";
            document.getElementById("menu").src = "../img/croix.png";
        }
    }
    
}