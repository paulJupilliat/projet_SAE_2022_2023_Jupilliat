
function cache_grp() {
    var grp = document.getElementsByClassName('grp');
    for (var i = 0; i < grp.length; i++) {
        // si le checkbox est coché alors on cache la colonne
        if (document.getElementById('grp').checked) {
            grp[i].style.display = 'none';
            document.getElementById('grp1').style.display = 'none';
            // ajout de la checkbox ailleurs
            
        }
        else{
            grp[i].style.display = 'table-cell';
        }

    }
    if(document.getElementById('grp').checked){
        const btn_rea = document.getElementById('groupe');
        if (btn_rea == null) {
            document.getElementById("tableau").innerHTML = '<input type="checkbox" id="groupe" name="grp" value="grp" onclick="remettre_grp()" class="in_filtres"> <label id = "label_groupe" for="groupe">Groupe </label>' + document.getElementById("tableau").innerHTML;
        }
        else{
            btn_rea.style.display = 'inline';
            document.getElementById('label_groupe').style.display = 'inline';
        }
    }
    else{
        const btn_rea = document.getElementById('groupe');
        if (btn_rea != null) {
            document.getElementById('grp1').style.display = 'table-cell';
            document.getElementById('groupe').style.display = 'none';
            document.getElementById('label_groupe').style.display = 'none';
            document.getElementById('groupe').checked = false;
        }
        

    }

}
function remettre_grp(){
    document.getElementById('grp').checked = false;
    cache_grp();
}







function cache_etu(){
    var etu = document.getElementsByClassName('etu');
    for (var i = 0; i < etu.length; i++) {
        // si le checkbox est coché alors on cache la colonne
        if (document.getElementById('etu').checked) {
            etu[i].style.display = 'none';
            document.getElementById('grp0').style.display = 'none';
            // ajout de la checkbox ailleurs
            
        }
        else{
            etu[i].style.display = 'table-cell';
        }

    }
    if(document.getElementById('etu').checked){
        const btn_rea = document.getElementById('etud');
        if (btn_rea == null) {
            document.getElementById("tableau").innerHTML = '<input type="checkbox" id="etud" name="etu" value="etu" onclick="remettre_etu()" class="in_filtres"> <label id = "label_etud" for="etud">Etudiant </label>' +document.getElementById("tableau").innerHTML;
        }
        else{
            btn_rea.style.display = 'inline';
            document.getElementById('label_etud').style.display = 'inline';
        }
    }
    else{
        const btn_rea = document.getElementById('etud');
        if (btn_rea != null) {
            document.getElementById('grp0').style.display = 'table-cell';
            document.getElementById('etud').style.display = 'none';
            document.getElementById('label_etud').style.display = 'none';
            document.getElementById('etud').checked = false;
        }
        

    }
}

function remettre_etu(){
    document.getElementById('etu').checked = false;
    cache_etu();
}


// --------------------------------------


function cache_soutien() {
    var soutien = document.getElementsByClassName('soutien');
    for (var i = 0; i < soutien.length; i++) {
        // si le checkbox est coché alors on cache la colonne
        if (document.getElementById('soutien').checked) {
            soutien[i].style.display = 'none';
            document.getElementById('grp2').style.display = 'none';
            // ajout de la checkbox ailleurs
            
        }
        else{
            soutien[i].style.display = 'table-cell';
        }

    }
    if(document.getElementById('soutien').checked){
        const btn_rea = document.getElementById('sout');
        if (btn_rea == null) {
            document.getElementById("tableau").innerHTML = '<input type="checkbox" id="sout" name="sout" value="soutien" onclick="remettre_soutien()" class="in_filtres"> <label id = "label_sout" for="sout">Soutien </label>' + document.getElementById("tableau").innerHTML;
        }
        else{
            btn_rea.style.display = 'inline';
            document.getElementById('label_sout').style.display = 'inline';
        }
    }
    else{
        const btn_rea = document.getElementById('sout');
        if (btn_rea != null) {
            document.getElementById('grp2').style.display = 'table-cell';
            document.getElementById('sout').style.display = 'none';
            document.getElementById('label_sout').style.display = 'none';
            document.getElementById('sout').checked = false;
        }
        

    }

}
function remettre_soutien(){
    document.getElementById('soutien').checked = false;
    cache_soutien();
}





// ---------------------


function cache_matiere() {
    var mat = document.getElementsByClassName('mat');
    for (var i = 0; i < mat.length; i++) {
        // si le checkbox est coché alors on cache la colonne
        if (document.getElementById('mat').checked) {
            mat[i].style.display = 'none';
            document.getElementById('grp3').style.display = 'none';
            // ajout de la checkbox ailleurs
            
        }
        else{
            mat[i].style.display = 'table-cell';
        }

    }
    if(document.getElementById('mat').checked){
        const btn_rea = document.getElementById('matiere');
        if (btn_rea == null) {
            document.getElementById("tableau").innerHTML = '<input type="checkbox" id="matiere" name="matiere" value="mat" onclick="remettre_matiere()" class="in_filtres"> <label id = "label_matiere" for="matiere">Matiere </label>' + document.getElementById("tableau").innerHTML;
        }
        else{
            btn_rea.style.display = 'inline';
            document.getElementById('label_matiere').style.display = 'inline';
        }
    }
    else{
        const btn_rea = document.getElementById('matiere');
        if (btn_rea != null) {
            document.getElementById('grp3').style.display = 'table-cell';
            document.getElementById('matiere').style.display = 'none';
            document.getElementById('label_matiere').style.display = 'none';
            document.getElementById('matiere').checked = false;
        }
        

    }

}
function remettre_matiere(){
    document.getElementById('mat').checked = false;
    cache_matiere();
}


// ---------------------



function cache_commentaire() {
    var comm = document.getElementsByClassName('comm');
    console.log(comm)
    for (var i = 0; i < comm.length; i++) {
        // si le checkbox est coché alors on cache la colonne
        if (document.getElementById('comm').checked) {
            comm[i].style.display = 'none';
            document.getElementById('grp4').style.display = 'none';
            // ajout de la checkbox ailleurs
            
        }
        else{
            comm[i].style.display = 'table-cell';
        }

    }
    if(document.getElementById('comm').checked){
        const btn_rea = document.getElementById('commentaire');
        if (btn_rea == null) {
            document.getElementById("tableau").innerHTML = '<input type="checkbox" id="commentaire" name="commentaire" value="comm" onclick="remettre_commentaire()" class="in_filtres"> <label id = "label_commentaire" for="commentaire">Commentaire </label>' + document.getElementById("tableau").innerHTML ;
        }
        else{
            btn_rea.style.display = 'inline';
            document.getElementById('label_commentaire').style.display = 'inline';
        }
    }
    else{
        const btn_rea = document.getElementById('commentaire');
        if (btn_rea != null) {
            document.getElementById('grp4').style.display = 'table-cell';
            document.getElementById('commentaire').style.display = 'none';
            document.getElementById('label_commentaire').style.display = 'none';
            document.getElementById('commentaire').checked = false;
        }
        

    }

}
    
function remettre_commentaire(){
    document.getElementById('comm').checked = false;
    cache_commentaire();
}

function cache_colonne(){  

    var id =event.srcElement.id;
    //si le premier caractère est un q on l'enlève
    if(id.charAt(0) == 'q'){
        id_cb=id
        id = id.substring(1);
    }
    var classn = "question" + id;
    var grp = "grpq" + id;
    var col = document.getElementsByClassName(classn);
    for (var i = 0; i < col.length; i++) {
        // si le checkbox est coché alors on cache la colonne
        if (document.getElementById(id).checked) {
            col[i].style.display = 'none';
            document.getElementById(grp).style.display = 'none';
            // ajout de la checkbox ailleurs
            
        }
        else{
            col[i].style.display = 'table-cell';
        }

    }
    if(document.getElementById(id).checked){
        
        const btn_rea = document.getElementById('q'+id);
        if (btn_rea == null) {
            var htmlbt= '<input type="checkbox" id="q'+id+'" name="q'+id+'" value="'+id+'" onclick="remettre_colonne()" class="in_filtres"> <label id ="label_q'+id+'" for="q'+id+'">Question'+id+' </label>' + document.getElementById("tableau").innerHTML ;
            document.getElementById("tableau").innerHTML = htmlbt;
        }
        else{
            btn_rea.style.display = 'inline';
            document.getElementById('label_q'+id).style.display = 'inline';
        }
    }
    else{
        const btn_rea = document.getElementById('q'+id);
        if (btn_rea != null) {
            document.getElementById(grp).style.display = 'table-cell';
            document.getElementById('q'+id).style.display = 'none';
            document.getElementById('label_q'+id).style.display = 'none';
            document.getElementById('q'+id).checked = false;
        }
        

    }

}

function remettre_colonne(){
    var id =event.srcElement.id;
    document.getElementById(id).checked = false;
    cache_colonne();

}
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