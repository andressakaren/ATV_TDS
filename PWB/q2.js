// 2) Faça um script que leia três números inteiros, em seguida mostre o maior e o menor deles.

let a = 3
let b = 9
let c = 1

function maior_menor() {
    maior = Math.max(a, b, c)
    // console.log(maior)
    menor = Math.min(a, b, c)
    // console.log(menor)

    return [maior, menor]
}

let resposta = maior_menor()
// console.log(resposta)

for (let i = 0; i < resposta.length; i++) {
    if (i == 0) {
        console.log(`Maior = ${resposta[i]}`)
    } else { 
        console.log(`Menor = ${resposta[i]}`)
    }
}

// Saída esperada 
// Maior = 9
// Menor = 1