// 7) Desenvolva uma função que verifique se uma palavra é um palíndromo (lê-se da mesma forma da esquerda para a direita e vice-versa). Retorne true se for um palíndromo e false se não for.

palavra = 'omissíssimo'

function removerEspacos() {
    palavraSemEspacos = palavra.replace(/\s+/g, '').trim();
    return palavraSemEspacos
}

// console.log(removerEspacos())

function testePalindromo() {
    
    palavraSemEspacos = removerEspacos()
    palavraInvertida = palavraSemEspacos.split('').reverse().join('')

    console.log(palavraInvertida)

    if (palavraSemEspacos === palavraInvertida) {
        return true   
    } else {
        return false
    }

}

console.log(testePalindromo())