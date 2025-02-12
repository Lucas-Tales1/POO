const CRUD = require('./CRUD');
const fs = require('fs');

class Usuario extends CRUD {
    constructor(nome, numero_matricula, endereco, tel, email, historico_emprestimos) {
        super('usuarios.json');
        this.nome = nome;
        this.numero_matricula = numero_matricula;
        this.endereco = endereco;
        this.tel = tel;
        this.email = email;
        this.historico_emprestimos = historico_emprestimos;
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

module.exports = Usuario;
