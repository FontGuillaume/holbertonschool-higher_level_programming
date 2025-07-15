async function getTitle() {
    const url = "https://swapi-api.hbtn.io/api/films/?format=json";
    const response = await fetch(url);
    const data = await response.json();
    const results = data.results;
    const ul = document.getElementById("list_movies");
    results.forEach(film => {
        const li = document.createElement("li");
        li.textContent = film.title;
        ul.appendChild(li);
    });
}

getTitle();