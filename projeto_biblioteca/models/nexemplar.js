const CRUD = require('./CRUD');
const fs = require('fs');

class Exemplar extends CRUD {
    constructor(descricao, situacao, data_devolucao) {
        super('exemplares.json');
        this.descricao = descricao;
        this.situacao = situacao;
        this.data_devolucao = data_devolucao;
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

module.exports = Exemplar;
