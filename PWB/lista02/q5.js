// 5) Implemente uma classe “Autor” que possui como atributos o nome e sobrenome do
// autor e criar um método que imprima o nome completo (nome + sobrenome).
// Implemente uma classe chamada “Livro” com atributos para armazenar o título, o
// autor e o número de páginas do livro.

class Autor {
    constructor(nome, sobrenome) {
        this.nome = nome
        this.sobrenome = sobrenome
    }

    nomeAutor() {
        return `${this.nome} ${this.sobrenome}`
    }
}

class Livro{
    constructor(titulo, autor, numero_paginas){
        this.titulo = titulo
        this.autor = autor
        this.numero_paginas = numero_paginas
    }

    detalhes(){
        return `Título do livro: ${this.titulo}\nAutor: ${this.autor.nomeAutor()}\nNúmero de páginas: ${this.numero_paginas}`
    }
}


autor1 = new Autor('Andressa', 'Karen')
// nome_autor1 = autor1.nomeAutor()
// console.log(nome_autor1) 
console.log(autor1.nomeAutor())
livro1 = new Livro('Livro top', autor1, 299)
console.log(livro1.detalhes())