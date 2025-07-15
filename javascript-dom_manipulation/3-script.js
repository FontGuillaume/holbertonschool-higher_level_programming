const header = document.querySelector("#toggle_header");
header.addEventListener("click", function() {
    if (header.classList.contains("red")) {
        header.classList.remove("red");
        header.classList.add("green");
    } else {
        header.classList.remove("green");
        header.classList.add("red");
    }
});