function getById(id){
    return document.getElementById(id);
}

// Questao 01
let textoOrigem1 = getById('textoOrigem1');
textoOrigem1.addEventListener('keyup', () => {
    let textoDestino1 = getById('textoDestino1');
    textoDestino1.value = textoOrigem1.value;
});

// Questao 02
let textoOrigem2 = getById('textoOrigem2');
textoOrigem2.addEventListener('keyup', () => {
    let textoDestino2 = getById('textoDestino2');
    textoDestino2.value = textoOrigem2.value.toUpperCase();
});

// Questao 03
let selecionarEmocao = getById('selecionarEmocao');
let imagem1 = getById('imagem1');

selecionarEmocao.addEventListener('change', () => {
    let emocaoSelecionada = selecionarEmocao.value;
    
    if (emocaoSelecionada === 'alegria') {
        imagem1.src = 'https://recreio.uol.com.br/media/uploads/disney/alegria_divertidamente.jpg';
    } else if (emocaoSelecionada === 'tristeza') {
        imagem1.src = 'https://recreio.uol.com.br/media/uploads/2024/06/tristeza.jpeg';
    } else if (emocaoSelecionada === 'raiva') {
        imagem1.src = 'https://recreio.uol.com.br/media/uploads/2024/06/raiva.jpg';
    }
});
