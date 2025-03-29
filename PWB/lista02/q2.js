// 2) Implemente uma classe chamada “Aluno” que possua atributos para armazenar o nome, a matrícula e as notas de um aluno. Adicione métodos para calcular a média das notas e verificar a situação do aluno (aprovado ou reprovado) de acordo com as regras de onde você estuda ou estudou.

class Aluno {
    constructor(nome, matricula, notas) {
        this.nome = nome;
        this.matricula = matricula;
        this.notas = notas; // considerar um array 
    }

    media() {
        // let soma = 0
        // for (let i = 0; i < this.notas.length; i++) {
        //     soma += this.notas[i]
        // }

        let soma = this.notas.reduce((acumulador, nota) => acumulador + nota, 0);
        return (soma / this.notas.length).toFixed(2);
    }

    verificarSituacao() {
        const media = this.media();
        return media >= 7 ? 'Aprovado!' : 'Reprovado';
    }
}

const aluno1 = new Aluno('Andressa', '2024111', [0, 9, 10])
console.log('Media: ',aluno1.media())
console.log('Situação atual: ',aluno1.verificarSituacao())