const updt_text = document.querySelector("#update_header");
const header = document.querySelector("header");

updt_text.addEventListener("click", function() {
    header.innerHTML = ("New Header !!!");
});