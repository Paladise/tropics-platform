function filter() {
    var query = document.getElementById("search").value.toUpperCase();
    var sands = document.getElementsByClassName("sand");
    for(i = 0; i < sands.length; i++) {
        var header = sands[i].getElementsByClassName("sand-header")[0];
        var name = header.getElementsByClassName("sand-name")[0].textContent;
        var tag = header.getElementsByClassName("sand-tag")[0].textContent;

        if(name.toUpperCase().indexOf(query) > -1 || tag.toUpperCase().indexOf(query) > -1) {
            sands[i].style.display = "";
        }else{
            sands[i].style.display = "none";
        }
    }
}