async function buscarFilmes() {
    let pesquisa = document.getElementById("pesquisa").value;
    let resultados = document.getElementById("resultados");

    resultados.innerHTML = "Carregando...";

    let resposta = await fetch(
        "https://www.omdbapi.com/?apikey=38b4b85b&s=" + encodeURIComponent(pesquisa) + "&type=movie"
    );

    let dados = await resposta.json();

    resultados.innerHTML = "";

    if (dados.Response === "False") {
        resultados.innerHTML = "Nenhum filme encontrado.";
        return;
    }

    dados.Search.forEach(function(filme) {
        resultados.innerHTML += `
            <div class="filme">
                <img src="${filme.Poster}" alt="Pôster do filme">
                <h3>${filme.Title}</h3>
                <p>${filme.Year}</p>
            </div>
        `;
    });
}