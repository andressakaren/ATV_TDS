var botao1 = document.getElementById('botao1');
botao1.addEventListener('click', clickBotao);

function clickBotao() {
    var resultado = document.getElementById('resultado')
    var nome = document.getElementById('nome')
    resultado.innerHTML = `Bom dia, ${nome.value}`
}
