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
            document.getElementById("tableau").innerHTML += '<input type="checkbox" id="groupe" name="grp" value="grp" onclick="remettre_grp()"> <label id = "label_groupe" for="groupe">Groupe </label>';
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


function adapte_nb_colonnes() {
    // compte les checkbox cochées et soustraits ce nombre au colspan
    let compteur = 0;
    if (document.getElementById('etu').checked){
        compteur++;
    }
    if (document.getElementById('grp').checked){
        compteur++;
    }
    if (document.getElementById('soutien').checked){
        compteur++;
    }
    if (document.getElementById('mat').checked){
        compteur++;
    }
    if (document.getElementById('comm').checked){
        compteur++;
    }
    // je recupere le tableau et je modifie le html
    let tableau = document.getElementById('tableau');
    tableau.innerHTML = tableau.innerHTML.replace(/colspan="5"/, 'colspan="'+(5-compteur)+'"');

    

}