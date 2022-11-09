//lance la fonction une fois que la page est chargée
window.onload = change_nav;
function change_nav(){
    const id = document.cookie.split("=").pop();
    console.log(document.cookie);
    var nav = document.getElementById("menu");
    if (id=="prof"){
        nav.innerHTML='<label for="toggle" class="label_nav">☰</label>'+
        '<input type="checkbox" id="toggle">'+
        '<div class="main_pages">'+
           ' <a href="./Acceuil.html" id="navbar_home">'+
            '<img src="../img/acceuil_act.png" height="50em" alt="" height="60em"></a>'+
            '<a href="./ResQCM.html" class="navbar__links">Resultats QCM</a>'+
            '<a href="./res_sond.html" class="navbar__links">Sondages</a>'+
            '<a href="./Dispo.html" class="navbar__links">Disponibilité Enseignant</a>'+
            '<a href="/" class="navbar__links">Gerer ses disponibilités</a>'+
            '<a href="/" class="navbar__links">Voir le soutien</a>'+
            '<a href="./SuiviGenEtu.html" class="navbar__links">Suivi Etudiant</a>'+
            '<a href="./paramEns.html" class="navbar__links"><img src="../img/reglages.png" height="50em" alt=""></a>'+
            '<a href="./index.html" class="navbar__links"><img src="../img/deconnexion.png" height="40em" alt=""></a></div>'
    }
    else{
        nav.innerHTML='<label for="toggle" class="label_nav">☰</label><input type="checkbox" id="toggle"><div class="main_pages">'+
            '<a href="./Acceuil.html" id="navbar_home"><img src="../img/acceuil_act.png" height="50em" alt="" height="60em"></a>'+
            '<a href="./ResQCM.html" class="navbar__links">Resultats QCM</a>'+
            '<a href="./res_sond.html" class="navbar__links">Sondages</a>'+
            '<a href="./Dispo.html" class="navbar__links">Disponibilité Enseignant</a>'+
            '<a href="/" class="navbar__links">Voir le soutien</a>'+
            '<a href="./SuiviGenEtu.html" class="navbar__links">Suivi Etudiant</a>'+
            '<a href="./paramAdm.html" class="navbar__links"> <img src="../img/reglages.png" height="50em" alt=""></a>'+
            '<a href="./index.html" class="navbar__links"><img src="../img/deconnexion.png" height="40em" alt=""></a></div>'}
    if (id=="prof" && window.location.href.split("/").pop()=="Acceuil.html"){
        document.getElementById("recup_données_btn").style.display="none";
        document.getElementById("text_mail").style.display="none";
    }
}