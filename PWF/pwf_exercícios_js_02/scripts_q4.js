var botao1 = document.getElementById('botao1')
botao1.addEventListener('click', textLength)

function textLength() {
    var resultado1 = document.getElementById('resultado1')
    var texto1 = document.getElementById('texto1')
    var resposta1 = texto1.value
    resultado1.innerHTML = `Resultado = ${resposta1.length}`
}

var botao2 = document.getElementById('botao2')
botao2.addEventListener('click', textToLowerCase)

function textToLowerCase() {
    var resultado2 = document.getElementById('resultado2')
    var texto2 = document.getElementById('texto2')
    var resposta2 = texto2.value
    resultado2.innerHTML = `Resultado = ${resposta2.toLowerCase()}`
}

var botao3 = document.getElementById('botao3')
botao3.addEventListener('click', textReplace)

function textReplace() {
    var resultado3 = document.getElementById('resultado3')
    var texto3 = document.getElementById('texto3')
    var resposta3 = texto3.value
    resultado3.innerHTML = `Resultado = ${resposta3.replace('a','@').replace('e', '3').replace('i', '1').replace('o','0')}`
}

var botao4 = document.getElementById('botao4')
botao4.addEventListener('click', textTrim)

function textTrim() {
    var resultado4 = document.getElementById('resultado4')
    var texto4 = document.getElementById('texto4')
    var numero4 = texto4.value
    resultado4.innerHTML = `Resultado = ${numero4.trim()}`
}

