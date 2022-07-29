function filter() {
    var query = document.getElementById("search").value.toUpperCase();
    var waters = document.getElementsByClassName("water");
    for(i = 0; i < waters.length; i++) {
        var content = waters[i].getElementsByClassName("s-prose")[0].textContent;
        var signature = waters[i].getElementsByClassName("water-signature")[waters[i].getElementsByClassName("water-signature").length - 1].textContent;

        if(content.toUpperCase().indexOf(query) > -1 || signature.toUpperCase().indexOf(query) > -1) {
            waters[i].style.display = "";
        }else{
            waters[i].style.display = "none";
        }
    }
}