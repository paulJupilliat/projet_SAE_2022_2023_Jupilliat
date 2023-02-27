//lance la fonction une fois que la page est chargée
window.onload = change_nav;
function change_nav(){
    const id = document.cookie.split("=").pop();
    var nav = document.getElementById("menu");
    const urlact=window.location.href;
    const nom=urlact.split("/").pop();
    if (nom=="Acceuil.html"){
        var img_home="../img/acceuil_act.png"
    }
    else{
        var img_home="../img/acceuil.png"}
    if (nom=="paramAdm.html" || nom=="paramEns.html"){
        var img_param="../img/reglages_act.png"
    }
    else{
        var img_param="../img/reglages.png"}
    if (id=="prof"){
        nav.innerHTML='<label for="toggle" class="label_nav">☰</label>'+
        '<input type="checkbox" id="toggle">'+
        '<div class="main_pages">'+
           ' <a href="./Acceuil.html" id="navbar_home">'+
            '<img src="'+img_home+'" height="50em" alt="" height="60em"></a>'+
            '<a href="./ResQCM.html" class="navbar__links">Résultats QCM</a>'+
            '<a href="./res_sond.html" class="navbar__links">Sondages</a>'+
            '<a href="./Dispo.html" class="navbar__links">Disponibilités enseignants</a>'+
            '<a href="/" class="navbar__links">Gérer ses disponibilités</a>'+
            '<a href="./Soutien.html" class="navbar__links">Voir le soutien</a>'+
            '<a href="./SuiviGenEtu.html" class="navbar__links">Suivi Etudiant</a>'+
            '<a href="./paramEns.html" class="navbar__links"><img src="'+img_param+'" height="50em" alt=""></a>'+
            '<a href="./index.html" class="navbar__links"><img src="../img/deconnexion.png" height="40em" alt=""></a></div>'
    }
    else{
        nav.innerHTML='<label for="toggle" class="label_nav">☰</label><input type="checkbox" id="toggle"><div class="main_pages">'+
            '<a href="./Acceuil.html" id="navbar_home"><img src="'+img_home+'" height="50em" alt="" height="60em"></a>'+
            '<a href="./ResQCM.html" class="navbar__links">Résultats QCM</a>'+
            '<a href="./res_sond.html" class="navbar__links">Sondages</a>'+
            '<a href="./Dispo.html" class="navbar__links">Disponibilités enseignants</a>'+
            '<a href="./Soutien.html" class="navbar__links">Voir le soutien</a>'+
            '<a href="./SuiviGenEtu.html" class="navbar__links">Suivi Etudiant</a>'+
            '<a href="./paramAdm.html" class="navbar__links"> <img src="'+img_param+'" height="50em" alt=""></a>'+
            '<a href="./index.html" class="navbar__links"><img src="../img/deconnexion.png" height="40em" alt=""></a></div>'}
    if (id=="prof" && window.location.href.split("/").pop()=="Acceuil.html"){
        document.getElementsByClassName("donnees_btn").style.display="none";
        document.getElementById("text_mail").style.display="none";
    }
}