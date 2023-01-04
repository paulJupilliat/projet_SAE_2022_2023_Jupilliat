function load_data(){
    const select = document.getElementById("sem-select");
    const sem = select.options[select.selectedIndex].value;
    if (sem == "semaine6") {
        const id = document.cookie.split("=").pop();
        if (id=="prof"){
            document.getElementById("tab2").innerHTML= "<tbody><tr><td colspan='6'>Données non disponibles</td></tr></tbody>";
        }
    else {
        document.getElementById("labels").innerHTML='<thead id="titre_suivi"><tr><th id="titre_tableau_sondage" colspan="7"><H2>Soutien</H2></th>'+
            '</tr><tr><th id="titre_tableau_sondage" colspan="7"><h3>Groupes composés</h3></th></tr>'+
            '<tr class="colonnes"><th class="noms">Etudiant</th><th class="noms">Matière 1</th>'+
                '<th class="noms">Matière 2</th><th class="noms">Volontaire</th><th class="noms">Souhait</th>'+
                '<th class="noms">Matière retenue</th><th class="noms">Enseignant</th></tr></thead>';
        document.getElementById("tab2").innerHTML= '<tbody><tr><td><a href="./Suivie_etu.html">Paul</a></td>'+
            '<td>Note</td><td>Note</td><td>Oui</td><td>Python</td><td><input type="text"value="Python"></input></td>'+
            '<td><select id="profs"><option value="">Chabin</option><option value="prof1">Anglade</option>'+
            '<option value="prof2">Adobet</option><option value="prof3">Roza</option><option value="prof4">Arzouse</option>'+
                '<option value="prof5">Limet</option><option value="prof6">Pinsard</option></select></td></tr>'+
            '<tr><td><a href="./Suivie_etu.html">Paul</a></td>'+
            '<td>Note</td><td>Note</td><td>Oui</td><td>Python</td><td><input type="text"value="Python"></input></td>'+
            '<td><select id="profs"><option value="">Chabin</option><option value="prof1">Anglade</option>'+
            '<option value="prof2">Adobet</option><option value="prof3">Roza</option><option value="prof4">Arzouse</option>'+
            '<option value="prof5">Limet</option><option value="prof6">Pinsard</option></select></td></tr>'+
            '<tr><td><a href="./Suivie_etu.html">Paul</a></td>'+
            '<td>Note</td><td>Note</td><td>Oui</td><td>Python</td><td><input type="text"value="Python"></input></td>'+
            '<td><select id="profs"><option value="">Chabin</option><option value="prof1">Anglade</option>'+
            '<option value="prof2">Adobet</option><option value="prof3">Roza</option><option value="prof4">Arzouse</option>'+
            '<option value="prof5">Limet</option><option value="prof6">Pinsard</option></select></td></tr>'+
            '<tr><td><a href="./Suivie_etu.html">Paul</a></td>'+
            '<td>Note</td><td>Note</td><td>Oui</td><td>Python</td><td><input type="text"value="Python"></input></td>'+
            '<td><select id="profs"><option value="">Chabin</option><option value="prof1">Anglade</option>'+
            '<option value="prof2">Adobet</option><option value="prof3">Roza</option><option value="prof4">Arzouse</option>'+
            '<option value="prof5">Limet</option><option value="prof6">Pinsard</option></select></td></tr>'+
            '<tr><td><a href="./Suivie_etu.html">Paul</a></td>'+
            '<td>Note</td><td>Note</td><td>Oui</td><td>Python</td><td><input type="text"value="Python"></input></td>'+
            '<td><select id="profs"><option value="">Chabin</option><option value="prof1">Anglade</option>'+
            '<option value="prof2">Adobet</option><option value="prof3">Roza</option><option value="prof4">Arzouse</option>'+
            '<option value="prof5">Limet</option><option value="prof6">Pinsard</option></select></td></tr>'+
            '<tr><td><a href="./Suivie_etu.html">Paul</a></td>'+
            '<td>Note</td><td>Note</td><td>Oui</td><td>Python</td><td><input type="text"value="Python"></input></td>'+
            '<td><select id="profs"><option value="">Chabin</option><option value="prof1">Anglade</option>'+
            '<option value="prof2">Adobet</option><option value="prof3">Roza</option><option value="prof4">Arzouse</option>'+
            '<option value="prof5">Limet</option><option value="prof6">Pinsard</option></select></td></tr>'+
            '<tr><td><a href="./Suivie_etu.html">Paul</a></td>'+
            '<td>Note</td><td>Note</td><td>Oui</td><td>Python</td><td><input type="text"value="Python"></input></td>'+
            '<td><select id="profs"><option value="">Chabin</option><option value="prof1">Anglade</option>'+
            '<option value="prof2">Adobet</option><option value="prof3">Roza</option><option value="prof4">Arzouse</option>'+
            '<option value="prof5">Limet</option><option value="prof6">Pinsard</option></select></td></tr>'+
            '<tr><td><a href="./Suivie_etu.html">Paul</a></td>'+
            '<td>Note</td><td>Note</td><td>Oui</td><td>Python</td><td><input type="text"value="Python"></input></td>'+
            '<td><select id="profs"><option value="">Chabin</option><option value="prof1">Anglade</option>'+
            '<option value="prof2">Adobet</option><option value="prof3">Roza</option><option value="prof4">Arzouse</option>'+
            '<option value="prof5">Limet</option><option value="prof6">Pinsard</option></select></td></tr>'+
            '<tr><td><a href="./Suivie_etu.html">Paul</a></td>'+
            '<td>Note</td><td>Note</td><td>Oui</td><td>Python</td><td><input type="text"value="Python"></input></td>'+
            '<td><select id="profs"><option value="">Chabin</option><option value="prof1">Anglade</option>'+
            '<option value="prof2">Adobet</option><option value="prof3">Roza</option><option value="prof4">Arzouse</option>'+
            '<option value="prof5">Limet</option><option value="prof6">Pinsard</option></select></td></tr>'+
            '<tr><td><a href="./Suivie_etu.html">Paul</a></td>'+
            '<td>Note</td><td>Note</td><td>Oui</td><td>Python</td><td><input type="text"value="Python"></input></td>'+
            '<td><select id="profs"><option value="">Chabin</option><option value="prof1">Anglade</option>'+
            '<option value="prof2">Adobet</option><option value="prof3">Roza</option><option value="prof4">Arzouse</option>'+
            '<option value="prof5">Limet</option><option value="prof6">Pinsard</option></select></td></tr>'+
            '<tr><td><a href="./Suivie_etu.html">Paul</a></td>'+
            '<td>Note</td><td>Note</td><td>Oui</td><td>Python</td><td><input type="text"value="Python"></input></td>'+
            '<td><select id="profs"><option value="">Chabin</option><option value="prof1">Anglade</option>'+
            '<option value="prof2">Adobet</option><option value="prof3">Roza</option><option value="prof4">Arzouse</option>'+
            '<option value="prof5">Limet</option><option value="prof6">Pinsard</option></select></td></tr>'+
            '<tr><td><a href="./Suivie_etu.html">Paul</a></td>'+
            '<td>Note</td><td>Note</td><td>Oui</td><td>Python</td><td><input type="text"value="Python"></input></td>'+
            '<td><select id="profs"><option value="">Chabin</option><option value="prof1">Anglade</option>'+
            '<option value="prof2">Adobet</option><option value="prof3">Roza</option><option value="prof4">Arzouse</option>'+
            '<option value="prof5">Limet</option><option value="prof6">Pinsard</option></select></td></tr>'+
            '<tr><td><a href="./Suivie_etu.html">Paul</a></td>'+
            '<td>Note</td><td>Note</td><td>Oui</td><td>Python</td><td><input type="text"value="Python"></input></td>'+
            '<td><select id="profs"><option value="">Chabin</option><option value="prof1">Anglade</option>'+
            '<option value="prof2">Adobet</option><option value="prof3">Roza</option><option value="prof4">Arzouse</option>'+
            '<option value="prof5">Limet</option><option value="prof6">Pinsard</option></select></td></tr>'+
            '<tr><td><a href="./Suivie_etu.html">Paul</a></td>'+
            '<td>Note</td><td>Note</td><td>Oui</td><td>Python</td><td><input type="text"value="Python"></input></td>'+
            '<td><select id="profs"><option value="">Chabin</option><option value="prof1">Anglade</option>'+
            '<option value="prof2">Adobet</option><option value="prof3">Roza</option><option value="prof4">Arzouse</option>'+
            '<option value="prof5">Limet</option><option value="prof6">Pinsard</option></select></td></tr>'+
            '<tr><td><a href="./Suivie_etu.html">Paul</a></td>'+
            '<td>Note</td><td>Note</td><td>Oui</td><td>Python</td><td><input type="text"value="Python"></input></td>'+
            '<td><select id="profs"><option value="">Chabin</option><option value="prof1">Anglade</option>'+
            '<option value="prof2">Adobet</option><option value="prof3">Roza</option><option value="prof4">Arzouse</option>'+
            '<option value="prof5">Limet</option><option value="prof6">Pinsard</option></select></td></tr>'+
            '<tr><td><a href="./Suivie_etu.html">Paul</a></td>'+
            '<td>Note</td><td>Note</td><td>Oui</td><td>Python</td><td><input type="text"value="Python"></input></td>'+
            '<td><select id="profs"><option value="">Chabin</option><option value="prof1">Anglade</option>'+
            '<option value="prof2">Adobet</option><option value="prof3">Roza</option><option value="prof4">Arzouse</option>'+
            '<option value="prof5">Limet</option><option value="prof6">Pinsard</option></select></td></tr>'+
            '<tr><td><a href="./Suivie_etu.html">Paul</a></td>'+
            '<td>Note</td><td>Note</td><td>Oui</td><td>Python</td><td><input type="text"value="Python"></input></td>'+
            '<td><select id="profs"><option value="">Chabin</option><option value="prof1">Anglade</option>'+
            '<option value="prof2">Adobet</option><option value="prof3">Roza</option><option value="prof4">Arzouse</option>'+
            '<option value="prof5">Limet</option><option value="prof6">Pinsard</option></select></td></tr>'+
            '<tr><td><a href="./Suivie_etu.html">Paul</a></td>'+
            '<td>Note</td><td>Note</td><td>Oui</td><td>Python</td><td><input type="text"value="Python"></input></td>'+
            '<td><select id="profs"><option value="">Chabin</option><option value="prof1">Anglade</option>'+
            '<option value="prof2">Adobet</option><option value="prof3">Roza</option><option value="prof4">Arzouse</option>'+
            '<option value="prof5">Limet</option><option value="prof6">Pinsard</option></select></td></tr></tbody>';
                
        document.getElementById("tableaugen").innerHTML += '<table id="labels"><thead id="titre_suivi"></tr><tr><th id="titre_tableau_sondage" colspan="7"><h3>Etudiants non volontaires qui pourraient avoir besoin</h3></th></tr>'+
        '<tr class="colonnes"><th class="noms">Etudiant</th><th class="noms">Matière 1</th>'+
            '<th class="noms">Matière 2</th><th class="noms">Volontaire</th><th class="noms">Souhait</th>'+
            '<th class="noms">Matière retenue</th><th class="noms">Ajouter</th></tr></thead></table>'+
        '<table class="scrolable" id="tab2"><tbody><tr><td><a href="./Suivie_etu.html">Paul</a></td>'+
        '<td>Note</td><td>Note</td><td>Non</td><td>Python</td><td><input type="text" value="Python"></input></td>'+
        '<td><button onclick="ajt_grp()">Ajouter au groupes</button></td></tr>'+
        '<tr><td><a href="./Suivie_etu.html">Paul</a></td>'+
        '<td>Note</td><td>Note</td><td>Non</td><td>Python</td><td><input type="text" value="Python"></input></td>'+
        '<td><button onclick="ajt_grp()">Ajouter au groupes</button></td></tr>'+
        '<tr><td><a href="./Suivie_etu.html">Paul</a></td>'+
        '<td>Note</td><td>Note</td><td>Non</td><td>Python</td><td><input type="text" value="Python"></input></td>'+
        '<td><button onclick="ajt_grp()">Ajouter au groupes</button></td></tr>'+
        '<tr><td><a href="./Suivie_etu.html">Paul</a></td>'+
        '<td>Note</td><td>Note</td><td>Non</td><td>Python</td><td><input type="text" value="Python"></input></td>'+
        '<td><button onclick="ajt_grp()">Ajouter au groupes</button></td></tr>'+
        '<tr><td><a href="./Suivie_etu.html">Paul</a></td>'+
        '<td>Note</td><td>Note</td><td>Non</td><td>Python</td><td><input type="text" value="Python"></input></td>'+
        '<td><button onclick="ajt_grp()">Ajouter au groupes</button></td></tr>'+
        '<tr><td><a href="./Suivie_etu.html">Paul</a></td>'+
        '<td>Note</td><td>Note</td><td>Non</td><td>Python</td><td><input type="text" value="Python"></input></td>'+
        '<td><button onclick="ajt_grp()">Ajouter au groupes</button></td></tr>'+
        '<tr><td><a href="./Suivie_etu.html">Paul</a></td>'+
        '<td>Note</td><td>Note</td><td>Non</td><td>Python</td><td><input type="text" value="Python"></input></td>'+
        '<td><button onclick="ajt_grp()">Ajouter au groupes</button></td></tr>'+
        '<tr><td><a href="./Suivie_etu.html">Paul</a></td>'+
        '<td>Note</td><td>Note</td><td>Non</td><td>Python</td><td><input type="text" value="Python"></input></td>'+
        '<td><button onclick="ajt_grp()">Ajouter au groupes</button></td></tr>'+
        '<tr><td><a href="./Suivie_etu.html">Paul</a></td>'+
        '<td>Note</td><td>Note</td><td>Non</td><td>Python</td><td><input type="text" value="Python"></input></td>'+
        '<td><button onclick="ajt_grp()">Ajouter au groupes</button></td></tr>'+
        '<tr><td><a href="./Suivie_etu.html">Paul</a></td>'+
        '<td>Note</td><td>Note</td><td>Non</td><td>Python</td><td><input type="text" value="Python"></input></td>'+
        '<td><button onclick="ajt_grp()">Ajouter au groupes</button></td></tr></tbody';     
}}
else{
    document.getElementById("tab2").innerHTML='<tbody><tr><td><a href="./Suivie_etu.html">Paul</a></td>'+
        '<td>07/11</td><td>11A</td><td>BDD</td><td>Chabin</td>'+
        '<td>Lorem ipsum dazdza d dazdazdazdazdza faefafafazfazf azdazdadazdzdzdazd dazdazdazdaz</td></tr>'+
        '<tr><td><a href="./Suivie_etu.html">Paul</a></td>'+
        '<td>07/11</td><td>11A</td><td>BDD</td><td>Chabin</td>'+
        '<td>Lorem ipsum dazdza d dazdazdazdazdza faefafafazfazf azdazdadazdzdzdazd dazdazdazdaz</td></tr>'+
        '<tr><td><a href="./Suivie_etu.html">Paul</a></td>'+
        '<td>07/11</td><td>11A</td><td>BDD</td><td>Chabin</td>'+
        '<td>Lorem ipsum dazdza d dazdazdazdazdza faefafafazfazf azdazdadazdzdzdazd dazdazdazdaz</td></tr>'+
        '<tr><td><a href="./Suivie_etu.html">Paul</a></td>'+
        '<td>07/11</td><td>11A</td><td>BDD</td><td>Chabin</td>'+
        '<td>Lorem ipsum dazdza d dazdazdazdazdza faefafafazfazf azdazdadazdzdzdazd dazdazdazdaz</td></tr>'+
        '<tr><td><a href="./Suivie_etu.html">Paul</a></td>'+
        '<td>07/11</td><td>11A</td><td>BDD</td><td>Chabin</td>'+
        '<td>Lorem ipsum dazdza d dazdazdazdazdza faefafafazfazf azdazdadazdzdzdazd dazdazdazdaz</td></tr>'+
        '<tr><td><a href="./Suivie_etu.html">Paul</a></td>'+
        '<td>07/11</td><td>11A</td><td>BDD</td><td>Chabin</td>'+
        '<td>Lorem ipsum dazdza d dazdazdazdazdza faefafafazfazf azdazdadazdzdzdazd dazdazdazdaz</td></tr>'+
        '<tr><td><a href="./Suivie_etu.html">Paul</a></td>'+
        '<td>07/11</td><td>11A</td><td>BDD</td><td>Chabin</td>'+
        '<td>Lorem ipsum dazdza d dazdazdazdazdza faefafafazfazf azdazdadazdzdzdazd dazdazdazdaz</td></tr>'+
        '<tr><td><a href="./Suivie_etu.html">Paul</a></td>'+
        '<td>07/11</td><td>11A</td><td>BDD</td><td>Chabin</td>'+
        '<td>Lorem ipsum dazdza d dazdazdazdazdza faefafafazfazf azdazdadazdzdzdazd dazdazdazdaz</td></tr>'+
        '<tr><td><a href="./Suivie_etu.html">Paul</a></td>'+
        '<td>07/11</td><td>11A</td><td>BDD</td><td>Chabin</td>'+
        '<td>Lorem ipsum dazdza d dazdazdazdazdza faefafafazfazf azdazdadazdzdzdazd dazdazdazdaz</td></tr>'+
        '<tr><td><a href="./Suivie_etu.html">Paul</a></td>'+
        '<td>07/11</td><td>11A</td><td>BDD</td><td>Chabin</td>'+
        '<td>Lorem ipsum dazdza d dazdazdazdazdza faefafafazfazf azdazdadazdzdzdazd dazdazdazdaz</td></tr>'+
        '<tr><td><a href="./Suivie_etu.html">Paul</a></td>'+
        '<td>07/11</td><td>11A</td><td>BDD</td><td>Chabin</td>'+
        '<td>Lorem ipsum dazdza d dazdazdazdazdza faefafafazfazf azdazdadazdzdzdazd dazdazdazdaz</td></tr>'+
        '<tr><td><a href="./Suivie_etu.html">Paul</a></td>'+
        '<td>07/11</td><td>11A</td><td>BDD</td><td>Chabin</td>'+
        '<td>Lorem ipsum dazdza d dazdazdazdazdza faefafafazfazf azdazdadazdzdzdazd dazdazdazdaz</td></tr>'+
        '<tr><td><a href="./Suivie_etu.html">Paul</a></td>'+
        '<td>07/11</td><td>11A</td><td>BDD</td><td>Chabin</td>'+
        '<td>Lorem ipsum dazdza d dazdazdazdazdza faefafafazfazf azdazdadazdzdzdazd dazdazdazdaz</td></tr>'+
        '<tr><td><a href="./Suivie_etu.html">Paul</a></td>'+
        '<td>07/11</td><td>11A</td><td>BDD</td><td>Chabin</td>'+
        '<td>Lorem ipsum dazdza d dazdazdazdazdza faefafafazfazf azdazdadazdzdzdazd dazdazdazdaz</td></tr>'+
        '<tr><td><a href="./Suivie_etu.html">Paul</a></td>'+
        '<td>07/11</td><td>11A</td><td>BDD</td><td>Chabin</td>'+
        '<td>Lorem ipsum dazdza d dazdazdazdazdza faefafafazfazf azdazdadazdzdzdazd dazdazdazdaz</td></tr>'+
        '<tr><td><a href="./Suivie_etu.html">Paul</a></td>'+
        '<td>07/11</td><td>11A</td><td>BDD</td><td>Chabin</td>'+
        '<td>Lorem ipsum dazdza d dazdazdazdazdza faefafafazfazf azdazdadazdzdzdazd dazdazdazdaz</td></tr>'+
        '<tr><td><a href="./Suivie_etu.html">Paul</a></td>'+
        '<td>07/11</td><td>11A</td><td>BDD</td><td>Chabin</td>'+
        '<td>Lorem ipsum dazdza d dazdazdazdazdza faefafafazfazf azdazdadazdzdzdazd dazdazdazdaz</td></tr>'+
        '<tr><td><a href="./Suivie_etu.html">Paul</a></td>'+
        '<td>07/11</td><td>11A</td><td>BDD</td><td>Chabin</td>'+
        '<td>Lorem ipsum dazdza d dazdazdazdazdza faefafafazfazf azdazdadazdzdzdazd dazdazdazdaz</td></tr>'+
        '<tr><td><a href="./Suivie_etu.html">Paul</a></td>'+
        '<td>07/11</td><td>11A</td><td>BDD</td><td>Chabin</td>'+
        '<td>Lorem ipsum dazdza d dazdazdazdazdza faefafafazfazf azdazdadazdzdzdazd dazdazdazdaz</td></tr>'+
        '<tr><td><a href="./Suivie_etu.html">Paul</a></td>'+
        '<td>07/11</td><td>11A</td><td>BDD</td><td>Chabin</td>'+
        '<td>Lorem ipsum dazdza d dazdazdazdazdza faefafafazfazf azdazdadazdzdzdazd dazdazdazdaz</td></tr>'+
   '<tr><td><a href="./Suivie_etu.html">Paul</a></td>'+
        '<td>07/11</td><td>11A</td><td>BDD</td><td>Chabin</td>'+
        '<td>Lorem ipsum dazdza d dazdazdazdazdza faefafafazfazf azdazdadazdzdzdazd dazdazdazdaz</td></tr>'+
   '<tr><td><a href="./Suivie_etu.html">Paul</a></td>'+
        '<td>07/11</td><td>11A</td><td>BDD</td><td>Chabin</td>'+
        '<td>Lorem ipsum dazdza d dazdazdazdazdza faefafafazfazf azdazdadazdzdzdazd dazdazdazdaz</td></tr>'+
        '<tr><td><a href="./Suivie_etu.html">Paul</a></td>'+
        '<td>07/11</td><td>11A</td><td>BDD</td><td>Chabin</td>'+
        '<td>Lorem ipsum dazdza d dazdazdazdazdza faefafafazfazf azdazdadazdzdzdazd dazdazdazdaz</td></tr>'+
        '<tr><td><a href="./Suivie_etu.html">Paul</a></td>'+
        '<td>07/11</td><td>11A</td><td>BDD</td><td>Chabin</td>'+
        '<td>Lorem ipsum dazdza d dazdazdazdazdza faefafafazfazf azdazdadazdzdzdazd dazdazdazdaz</td></tr>'+
        '<tr><td><a href="./Suivie_etu.html">Paul</a></td>'+
        '<td>07/11</td><td>11A</td><td>BDD</td><td>Chabin</td>'+
        '<td>Lorem ipsum dazdza d dazdazdazdazdza faefafafazfazf azdazdadazdzdzdazd dazdazdazdaz</td></tr>'+
        '<tr><td><a href="./Suivie_etu.html">Paul</a></td>'+
        '<td>07/11</td><td>11A</td><td>BDD</td><td>Chabin</td>'+
        '<td>Lorem ipsum dazdza d dazdazdazdazdza faefafafazfazf azdazdadazdzdzdazd dazdazdazdaz</td></tr>'+
   '<tr><td><a href="./Suivie_etu.html">Paul</a></td>'+
        '<td>07/11</td><td>11A</td><td>BDD</td><td>Chabin</td>'+
        '<td>Lorem ipsum dazdza d dazdazdazdazdza faefafafazfazf azdazdadazdzdzdazd dazdazdazdaz</td></tr>'+
        '<tr><td><a href="./Suivie_etu.html">Paul</a></td>'+
        '<td>07/11</td><td>11A</td><td>BDD</td><td>Chabin</td>'+
        '<td>Lorem ipsum dazdza d dazdazdazdazdza faefafafazfazf azdazdadazdzdzdazd dazdazdazdaz</td></tr>'+
        '<tr><td><a href="./Suivie_etu.html">Paul</a></td>'+
        '<td>07/11</td><td>11A</td><td>BDD</td><td>Chabin</td>'+
        '<td>Lorem ipsum dazdza d dazdazdazdazdza faefafafazfazf azdazdadazdzdzdazd dazdazdazdaz</td></tr>'+
   '<tr><td><a href="./Suivie_etu.html">Paul</a></td>'+
        '<td>07/11</td><td>11A</td><td>BDD</td><td>Chabin</td>'+
        '<td>Lorem ipsum dazdza d dazdazdazdazdza faefafafazfazf azdazdadazdzdzdazd dazdazdazdaz</td></tr>'+
        '<tr><td><a href="./Suivie_etu.html">Paul</a></td>'+
        '<td>07/11</td><td>11A</td><td>BDD</td><td>Chabin</td>'+
        '<td>Lorem ipsum dazdza d dazdazdazdazdza faefafafazfazf azdazdadazdzdzdazd dazdazdazdaz</td></tr>'+
        '<tr><td><a href="./Suivie_etu.html">Paul</a></td>'+
        '<td>07/11</td><td>11A</td><td>BDD</td><td>Chabin</td>'+
        '<td>Lorem ipsum dazdza d dazdazdazdazdza faefafafazfazf azdazdadazdzdzdazd dazdazdazdaz</td></tr>'+
        '<tr><td><a href="./Suivie_etu.html">Paul</a></td>'+
        '<td>07/11</td><td>11A</td><td>BDD</td><td>Chabin</td>'+
        '<td>Lorem ipsum dazdza d dazdazdazdazdza faefafafazfazf azdazdadazdzdzdazd dazdazdazdaz</td></tr>'+
   '<tr><td><a href="./Suivie_etu.html">Paul</a></td>'+
        '<td>07/11</td><td>11A</td><td>BDD</td><td>Chabin</td>'+
        '<td>Lorem ipsum dazdza d dazdazdazdazdza faefafafazfazf azdazdadazdzdzdazd dazdazdazdaz</td></tr>'+
   '<tr><td><a href="./Suivie_etu.html">Paul</a></td>'+
        '<td>07/11</td><td>11A</td><td>BDD</td><td>Chabin</td>'+
        '<td>Lorem ipsum dazdza d dazdazdazdazdza faefafafazfazf azdazdadazdzdzdazd dazdazdazdaz</td></tr>'+
        '<tr><td><a href="./Suivie_etu.html">Paul</a></td>'+
        '<td>07/11</td><td>11A</td><td>BDD</td><td>Chabin</td>'+
        '<td>Lorem ipsum dazdza d dazdazdazdazdza faefafafazfazf azdazdadazdzdzdazd dazdazdazdaz</td></tr>'+
        '<tr><td><a href="./Suivie_etu.html">Paul</a></td>'+
        '<td>07/11</td><td>11A</td><td>BDD</td><td>Chabin</td>'+
        '<td>Lorem ipsum dazdza d dazdazdazdazdza faefafafazfazf azdazdadazdzdzdazd dazdazdazdaz</td></tr>'+
        '<tr><td><a href="./Suivie_etu.html">Paul</a></td>'+
        '<td>07/11</td><td>11A</td><td>BDD</td><td>Chabin</td>'+
        '<td>Lorem ipsum dazdza d dazdazdazdazdza faefafafazfazf azdazdadazdzdzdazd dazdazdazdaz</td></tr>'+
   '<tr><td><a href="./Suivie_etu.html">Paul</a></td>'+
        '<td>07/11</td><td>11A</td><td>BDD</td><td>Chabin</td>'+
        '<td>Lorem ipsum dazdza d dazdazdazdazdza faefafafazfazf azdazdadazdzdzdazd dazdazdazdaz</td></tr>'+
   '<tr><td><a href="./Suivie_etu.html">Paul</a></td>'+
        '<td>07/11</td><td>11A</td><td>BDD</td><td>Chabin</td>'+
        '<td>Lorem ipsum dazdza d dazdazdazdazdza faefafafazfazf azdazdadazdzdzdazd dazdazdazdaz</td></tr>'+
        '<tr><td><a href="./Suivie_etu.html">Paul</a></td>'+
        '<td>07/11</td><td>11A</td><td>BDD</td><td>Chabin</td>'+
        '<td>Lorem ipsum dazdza d dazdazdazdazdza faefafafazfazf azdazdadazdzdzdazd dazdazdazdaz</td></tr>'+
        '<tr><td><a href="./Suivie_etu.html">Paul</a></td>'+
        '<td>07/11</td><td>11A</td><td>BDD</td><td>Chabin</td>'+
        '<td>Lorem ipsum dazdza d dazdazdazdazdza faefafafazfazf azdazdadazdzdzdazd dazdazdazdaz</td></tr>'+
        '<tr><td><a href="./Suivie_etu.html">Paul</a></td>'+
        '<td>07/11</td><td>11A</td><td>BDD</td><td>Chabin</td>'+
        '<td>Lorem ipsum dazdza d dazdazdazdazdza faefafafazfazf azdazdadazdzdzdazd dazdazdazdaz</td></tr>'+
        '<tr><td><a href="./Suivie_etu.html">Paul</a></td>'+
        '<td>07/11</td><td>11A</td><td>BDD</td><td>Chabin</td>'+
        '<td>Lorem ipsum dazdza d dazdazdazdazdza faefafafazfazf azdazdadazdzdzdazd dazdazdazdaz</td></tr>'+
        '<tr><td><a href="./Suivie_etu.html">Paul</a></td>'+
        '<td>07/11</td><td>11A</td><td>BDD</td><td>Chabin</td>'+
        '<td>Lorem ipsum dazdza d dazdazdazdazdza faefafafazfazf azdazdadazdzdzdazd dazdazdazdaz</td></tr>'+
        '<tr><td><a href="./Suivie_etu.html">Paul</a></td>'+
        '<td>07/11</td><td>11A</td><td>BDD</td><td>Chabin</td>'+
        '<td>Lorem ipsum dazdza d dazdazdazdazdza faefafafazfazf azdazdadazdzdzdazd dazdazdazdaz</td></tr>'+
        '<tr><td><a href="./Suivie_etu.html">Paul</a></td>'+
        '<td>07/11</td><td>11A</td><td>BDD</td><td>Chabin</td>'+
        '<td>Lorem ipsum dazdza d dazdazdazdazdza faefafafazfazf azdazdadazdzdzdazd dazdazdazdaz</td></tr></tbody>';
   
    
}}