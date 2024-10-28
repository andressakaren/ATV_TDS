var botao1 = document.getElementById('botao1')
botao1.addEventListener('click', numRandom)

function numRandom() {
    var resultado1 = document.getElementById('resultado1')
    var numero1 = parseInt(Math.random() * 10)
    resultado1.innerHTML = `Resultado = ${numero1}`
}

var botao2 = document.getElementById('botao2')
botao2.addEventListener('click', numAbs)

function numAbs() {
    var resultado2 = document.getElementById('resultado2')
    var texto2 = document.getElementById('texto2')
    var numero2 = Math.abs(parseFloat(texto2.value))
    resultado2.innerHTML = `Resultado = ${numero2}`
}

var botao3 = document.getElementById('botao3')
botao3.addEventListener('click', numMax)

function numMax() {
    var resultado3 = document.getElementById('resultado3')
    var texto3_1 = document.getElementById('texto3_1')
    var texto3_2 = document.getElementById('texto3_2')
    var numero3 = Math.max(texto3_1.value, texto3_2.value)
    resultado3.innerHTML = `Resultado = ${numero3}`
}

var botao4 = document.getElementById('botao4')
botao4.addEventListener('click', numRound)

function numRound() {
    var resultado4 = document.getElementById('resultado4')
    var texto4 = document.getElementById('texto4')
    var numero4 = Math.round(texto4.value)
    resultado4.innerHTML = `Resultado = ${numero4}`
}

var botao5 = document.getElementById('botao5')
botao5.addEventListener('click', numPow)

function numPow() {
    var resultado5 = document.getElementById('resultado5')
    var texto5_1 = document.getElementById('texto5_1')
    var texto5_2 = document.getElementById('texto5_2')
    var numero5 = Math.pow(texto5_1.value, texto5_2.value)
    resultado5.innerHTML = `Resultado = ${numero5}`
}