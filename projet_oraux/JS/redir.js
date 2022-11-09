function redirection(id,dir){
    const urlact=window.location.href;
    const nom=urlact.split("/").pop();
    console.log(nom);
    const url=urlact.replace(nom,dir+".html");
    if (nom=="connexionAdm.html" || nom=="connexionProf.html"){
    document.cookie=id;}
    window.location.href = url;
}
