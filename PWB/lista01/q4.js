// Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.

let a = 80000
let b = 200000
let count = 0

while (a <= b) {
    a = a*1.03;
    // console.log(a)
    b = b*1.015;
    // console.log(b)
    count++;
}

console.log(`Número necessário de anos: ${count} anos.`)