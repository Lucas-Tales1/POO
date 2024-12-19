from models.produto import Produto

class Carrinho:
    def __init__(self):
        self.itens = []

    def inserir(self, produto, quantidade):
        for i, item in enumerate(self.itens):
            if item[0].id == produto.id:
                self.itens[i] = (item[0], item[1] + quantidade)
                return
        self.itens.append((produto, quantidade))

    def remover_item(self, produto_id):
        self.itens = [item for item in self.itens if item[0].id != produto_id]

    def listar_itens(self):
        return self.itens

    def esvaziar(self):
        self.itens = []

    def salvar(self):
        return [{'id': item[0].id, 'descricao': item[0].descricao, 'preco': item[0].preco, 'quantidade': item[1]} for item in self.itens]

    def abrir(self, itens):
        self.itens = []
        for item in itens:
            produto = Produto(item['id'], item['descricao'], item['preco'], 0, None)
            self.inserir(produto, item['quantidade'])
