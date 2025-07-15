const item = document.querySelector("#add_item");
const add_list = document.querySelector(".my_list")
item.addEventListener("click", function() {
    const new_li = document.createElement("li");
    new_li.setAttribute("class", "my_list");
    new_li.innerHTML = "Item";
    add_list.appendChild(new_li)
    

})