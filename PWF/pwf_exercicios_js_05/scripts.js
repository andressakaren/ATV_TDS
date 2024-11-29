function getById(id) {
    return document.getElementById(id);
}

// QUESTAO 01

let box = getById('box');
let aparecerImagem = getById('aparecerImagem');

aparecerImagem.addEventListener('click', () => {
    if (box.style.visibility === 'hidden') {
        box.style.visibility = 'visible';
    } else {
        box.style.visibility = 'hidden';
    }
});

// QUESTAO 02
let texto = getById('texto');
let aumentarFonte = getById('aumentarFonte');
let reduzirFonte = getById('reduzirFonte');

aumentarFonte.addEventListener('click', () => alterarTamanhoFonte(2));

reduzirFonte.addEventListener('click', () => alterarTamanhoFonte(-2));

function alterarTamanhoFonte(valor) {
    texto.style.fontSize = '16px';

    let tamanhoAtual = parseInt(texto.style.fontSize);
    let novoTamanho = tamanhoAtual + valor;

    texto.style.fontSize = novoTamanho + 'px';
}

// QUESTAO 03
let horaInserida = getById('hora');
let verificarHora = getById('verificarHora');

verificarHora.addEventListener('click', () => {
    let hora = parseInt(horaInserida.value); // converte p número inteiro

    if ((hora >= 18 && hora <= 23) || (hora >= 0 && hora <= 6)) {
        document.body.style.backgroundColor = 'black'; 
        document.body.style.color = 'white'; 
    } else {
        document.body.style.backgroundColor = 'white';
        document.body.style.color = 'black'; 
    }
});

// QUESTAO 04
let caixaClasse  = getById('caixaClasse');
let alterarClasse = getById('alterarClasse');

alterarClasse.addEventListener('click', () => {
    caixaClasse.classList.toggle('novoEstilo');
})
