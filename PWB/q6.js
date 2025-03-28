// 6) Implemente uma função que recebe como parâmetro um array de números, calcule a média aritmética e retorne o resultado.


let array = [50, 5, 8, 10, 22]

soma = 0
function mediaAritmetica() {
    for (let i=0; i < array.length; i++) {
        soma += array[i]
    }
    resultado = soma / array.length
    return Math.round((resultado))
}

console.log(mediaAritmetica())

