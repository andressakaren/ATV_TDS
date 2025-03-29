// 1) Crie uma classe chamada “Círculo” que possua um atributo para armazenar o raio
// e métodos para calcular a área e o perímetro do círculo.

class Circulo {
    constructor(raio) {
        this.raio = raio;
    }

    area() {
        return Number((Math.PI * (this.raio ** 2)).toFixed(2)); 
    }

    perimetro() {
        return Number((2 * Math.PI * this.raio).toFixed(2)); 
    }
}

// Criar um objeto NEW
const circulo1 = new Circulo(2)

console.log(`Área: ${circulo1.area()}`)
console.log(`Perímetro: ${circulo1.perimetro()}`)