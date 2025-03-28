// Dado o array numeros, crie um novo array chamado numerosUnicos, contendo os mesmos elementos do array original, mas sem valores repetidos e exibir no console.
// const numeros = [3, 7, 3, 2, 7, 10, 2, 15, 10, 20];

const numeros = [3, 7, 3, 2, 7, 10, 2, 15, 10, 20];

// let arreyNumerosUnicos = [];

// for (let i = 0; i < numeros.length; i++) {
//     if (!arreyNumerosUnicos.includes(numeros[i])) {
//         arreyNumerosUnicos.push(numeros[i])
//     } 
// }

let arrayNumerosUnicos_SET = [...new Set(numeros)];
console.log(arrayNumerosUnicos_SET)
