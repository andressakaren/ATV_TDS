var botao1 = document.getElementById('botao1')
botao1.addEventListener('click', nomeCompleto)

function nomeCompleto() {
    var resultado1 = document.getElementById('resultado1')
    var texto1_1 = document.getElementById('texto1_1')
    var texto1_2 = document.getElementById('texto1_2')
    var resposta1 = `${texto1_1.value} ${texto1_2.value}`
    resultado1.innerHTML = `Resultado = ${resposta1}`
}

var botao2 = document.getElementById('botao2')
botao2.addEventListener('click', operacaoNumeros)

function operacaoNumeros() {
    var resultado2 = document.getElementById('resultado2')
    var texto2_1 = document.getElementById('texto2_1')
    var texto2_2 = document.getElementById('texto2_2')
    var resposta2_1 = parseFloat(texto2_1.value)
    var resposta2_2 = parseFloat(texto2_2.value)
    resultado2.innerHTML = `Resultado soma = ${resposta2_1 + resposta2_2} Resultado subtração = ${resposta2_1 - resposta2_2}`
}

var botao3 = document.getElementById('botao3')
botao3.addEventListener('click', limparCaixa)

function limparCaixa() {
    document.getElementById("texto3").value = "";
}

var botao4 = document.getElementById('botao4')
botao4.addEventListener('click', copiarTexto)

function copiarTexto() {
    var resposta4 = document.getElementById("texto4_1").value;
    document.getElementById("texto4_2").value = resposta4;
}