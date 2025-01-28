const lolApi = "https://ddragon.leagueoflegends.com/cdn/13.1.1/data/en_US/champion.json";
const translateApi = "https://api.mymemory.translated.net/get?q="; // MyMemory Translation API

async function traduzirTexto(text) {
    try {
        const response = await fetch(`${translateApi}${encodeURIComponent(text)}&langpair=en|pt-br`);
        const data = await response.json();
        return data.responseData.translatedText; // json
    } catch (error) {
        console.error('Erro ao traduzir o texto:', error);
        return text; // Retorna o original se der erro..
    }
}

document.getElementById('campeao-btn').addEventListener('click', async () => {
    const campeaoNome = document.getElementById('campeao-input').value;
    fetch(lolApi)
        .then(response => response.json())
        .then(async (data) => {
            const campeaoData = data.data[campeaoNome];
            const lolResultado = document.getElementById('lol-resultados');

            if (campeaoData) {
                const translatedBlurb = await traduzirTexto(campeaoData.blurb);
                const translatedTitle = await traduzirTexto(campeaoData.title);
                lolResultado.innerHTML = `
                    <h3>${campeaoData.name}</h3>
                    <p>${translatedTitle}</p>
                    <p><br>${translatedBlurb}</p>
                `;
            } else {
                lolResultado.innerHTML = '<p>Campeão não encontrado.</p>';
            }
        })
        .catch(error => console.error('Erro ao buscar dados do League of Legends:', error));
});
