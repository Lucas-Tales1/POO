const CRUD = require('./CRUD');
const fs = require('fs');

class Bibliotecario extends CRUD {
    constructor(nome, id) {
        super('bibliotecarios.json');
        this.nome = nome;
        this.id = id;
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

module.exports = Bibliotecario;
