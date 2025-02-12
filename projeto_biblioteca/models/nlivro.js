const CRUD = require('./CRUD');
const fs = require('fs');

class Livro extends CRUD {
    constructor(id, titulo, autor, genero, num_paginas, ano_publicacao, disponibilidade, qtd_total, qtd_disponivel) {
        super('livros.json');
        this.id = id;
        this.titulo = titulo;
        this.autor = autor;
        this.genero = genero;
        this.num_paginas = num_paginas;
        this.ano_publicacao = ano_publicacao;
        this.disponibilidade = disponibilidade;
        this.qtd_total = qtd_total;
        this.qtd_disponivel = qtd_disponivel;
    }

    abrir() {
        return this.listar();
    }

    salvar() {
        const dados = this.listar();
        dados.push(this);
        fs.writeFileSync(this.caminhoArquivo, JSON.stringify(dados, null, 2));
    }
}

module.exports = Livro;
