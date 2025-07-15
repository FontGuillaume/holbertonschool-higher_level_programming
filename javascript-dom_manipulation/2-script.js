const redHeader = document.querySelector("#red_header"); // le div
const header = document.querySelector("header");         // le header

redHeader.addEventListener("click", function() {
    header.classList.add("red"); // on ajoute la classe au header
});