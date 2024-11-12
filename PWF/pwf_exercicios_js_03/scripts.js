function getById(id) {
    return document.getElementById(id);
}

function clique(id, funcao) {
    getById(id).addEventListener('click', funcao); 
}

// Qst 01
clique('botao1', () => {
    var num1 = getById('num1').value
    var padded = num1.padStart(5,"0");
    getById('resultado1').innerHTML = padded;
});

// Qst 02
clique('botao2', () => {
    var num2_1 = getById('num2_1').value
    var num2_2 = getById('num2_2').value
    getById('resultado2').innerHTML = 
    `
    Resultado 
    Soma: ${num2_1} + ${num2_2} = ${num2_1 + num2_2} <br> 
    Subtração: ${num2_1} - ${num2_2} = ${num2_1 - num2_2} <br> 
    Multiplicação: ${num2_1} * ${num2_2} = ${num2_1 * num2_2} <br>
    Divisão: ${num2_1} / ${num2_2} = ${(num2_1 / num2_2).toFixed(2)} <br> 
    `
})

// Qst 03
clique('botao3', () => {
    var num3 = getById('num3').value
    var Fahrenheit = (num3 * 1.8) + 32
    getById('resultado3').innerHTML = 
    `
    <br>
    Resultado em Fahrenheit:
    <br>
    Fórmula F = C x 1,8 + 32
    <br>
    Resultado: ${Fahrenheit}°F
    `
})

// Qst 04
clique('botao4', () => {
    var data = new Date()
    getById('resultado4').innerHTML = data
})

// Qst 05
function myFunction() {
    var fname = getById('fname');
    fname.value = fname.value.toUpperCase();
  }