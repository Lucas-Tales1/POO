const CRUD = require('./CRUD');
const fs = require('fs');

class Emprestimo extends CRUD {
    constructor(livro, usuario, data_emprestimo, data_devolucao, data_devolucao_real, id) {
        super('emprestimos.json');
        this.livro = livro;
        this.usuario = usuario;
        this.data_emprestimo = data_emprestimo;
        this.data_devolucao = data_devolucao;
        this.data_devolucao_real = data_devolucao_real;
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

module.exports = Emprestimo;
