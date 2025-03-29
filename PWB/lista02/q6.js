// 6) Modifique a questão anterior para que o livro possa ter mais de um autor e adicione um método que imprima o nome completo de seus autores.

class Autor {
    constructor(nome, sobrenome) {
        this.nome = nome
        this.sobrenome = sobrenome
    }

    nomeAutor() {
        return `${this.nome} ${this.sobrenome}`
    }
}

class Livro {
    constructor(titulo, autores, numero_paginas) {
        this.titulo = titulo
        this.autores = autores // arrey de autores
        this.numero_paginas = numero_paginas
    }

    nomeAutores() {
        let nomeAutores = ''
        for(let i = 0; i < this.autores.length; i++) {
            nomeAutores += `  ${this.autores[i].nomeAutor()}\n`
        }
        // console.log(nomeAutores)
        return nomeAutores
    }

    detalhes() {
        return `Título do livro:\n  ${this.titulo}\nAutores:\n${this.nomeAutores()}Número de páginas:\n  ${this.numero_paginas}`
    }
}


autor1 = new Autor('Andressa', 'Karen')
autor2 = new Autor('Edith', 'Ribeiro')
// nome_autor1 = autor1.nomeAutor()
// console.log(nome_autor1) 
// console.log(autor1.nomeAutor())
livro1 = new Livro('Livro top', [autor1, autor2], 299)
// console.log(livro1.detalhes())
// livro1.nomeAutores()
console.log(livro1.detalhes())
