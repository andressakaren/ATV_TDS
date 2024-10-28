var botao1 = document.getElementById('botao1');
botao1.addEventListener('click', bomDia);

var botao2 = document.getElementById('botao2');
botao2.addEventListener('click', boaNoite);

function bomDia() {
    var resultado = document.getElementById('resultado')
    resultado.innerHTML = 'Bom dia, flor do dia'
}

function boaNoite() {
    var resultado = document.getElementById('resultado')
    resultado.innerHTML = 'Boa noite, flor da noite'
}

