const fs = require('fs');

class CRUD {
    constructor(caminhoArquivo) {
        this.caminhoArquivo = caminhoArquivo;
    }

    inserir(item) {
        const dados = this.listar();
        dados.push(item);
        this.salvar(dados);
    }

    listar() {
        try {
            const dados = fs.readFileSync(this.caminhoArquivo, 'utf-8');
            return JSON.parse(dados);
        } catch (e) {
            return [];
        }
    }

    atualizar(id, novoItem) {
        let dados = this.listar();
        dados = dados.map(item => item.id === id ? novoItem : item);
        this.salvar(dados);
    }

    excluir(id) {
        let dados = this.listar();
        dados = dados.filter(item => item.id !== id);
        this.salvar(dados);
    }

    salvar(dados) {
        fs.writeFileSync(this.caminhoArquivo, JSON.stringify(dados, null, 2));
    }
}

module.exports = CRUD;
