function getByID(id) {
    return document.getElementById(id);
}

let botaoConsultar = getByID('botaoConsultar');
let botaoLimpar = getByID('botaoLimpar');
let botaoInverter = getByID('botaoInverter');

botaoConsultar.addEventListener('click', consultarPreco);
botaoLimpar.addEventListener('click', limparCampos);
botaoInverter.addEventListener('click', inverterMoedas);

async function consultarPreco() {
    let moedaBase = getByID('moedaBase').value.toUpperCase(); // Moeda base (ex.: BTC)
    let moedaConversao = getByID('moedaConversao').value.toUpperCase(); // Moeda de conversão (ex.: USDT)
    let resultado = getByID('resultado');

    // Validação de campos vazios: Antes de fazer a consulta, verificar se os campos moedaBase e moedaConversao foram preenchidos.
    if (!moedaBase || !moedaConversao) {
        resultado.innerHTML = 'Por favor, preencha ambos os campos antes de consultar.';
        return;
    }

    let url = `https://api.binance.com/api/v3/ticker/price?symbol=${moedaBase}${moedaConversao}`;

    try {
        let response = await fetch(url); // Faz a requisição à API Binance

        if (!response.ok) {
            throw new Error(`HTTP Error: ${response.status} - ${response.statusText}`);
        }
        let json = await response.json();

        resultado.innerHTML = `
        <p><strong>Par de Moedas:</strong> ${json.symbol}</p>
        <p><strong>Preço:</strong> ${parseFloat(json.price).toFixed(2)} ${moedaConversao}</p>`;
    } catch (error) {
        resultado.innerHTML = 'Erro: ' + error.message;
    }
}

// Botão de limpar campos: Um botão que limpa os campos de entrada (moedaBase, moedaConversao) e o resultado exibido;
function limparCampos() {
    getByID('moedaBase').value = '';
    getByID('moedaConversao').value = '';
    getByID('resultado').innerHTML = '';
}

// Botão de inverter moedas: Um botão que troca os valores das moedas base e de conversão;
function inverterMoedas() {
    let moedaBase = getByID('moedaBase');
    let moedaConversao = getByID('moedaConversao');

    let temp = moedaBase.value;
    moedaBase.value = moedaConversao.value;
    moedaConversao.value = temp;
}
