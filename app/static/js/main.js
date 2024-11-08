// Função para carregar os episódios da API
async function fetchEpisodes() {
    const response = await fetch("/episodes");  
    const episodes = await response.json();
    return episodes;
}

function renderEpisodes(episodes, seasonFilter = "") {
    const tableBody = document.querySelector("#episodes-table tbody");
    tableBody.innerHTML = "";  // Limpa a tabela antes de re-renderizar

    const filteredEpisodes = seasonFilter
        ? episodes.filter(episode => episode.season == seasonFilter)
        : episodes;

    filteredEpisodes.forEach(episode => {
        const row = document.createElement("tr");

        row.innerHTML = `
            <td>${episode.episode_name}</td>
            <td>${episode.season}</td>
            <td>${episode.episode_number}</td>
            <td>${episode.rating}</td>
        `;

        tableBody.appendChild(row);
    });
}


async function initialize() {
    const episodes = await fetchEpisodes();
    renderEpisodes(episodes);
    renderSeasonFilter(episodes);
}

window.onload = initialize;
