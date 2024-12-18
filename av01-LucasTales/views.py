from models.cliente import Cliente, Clientes
from models.categoria import Categoria, Categorias
from models.produto import Produto, Produtos
from models.venda import Venda, Vendas
from models.vendaItem import VendaItem, VendaItems

class View:
    @staticmethod
    def cliente_admin():
        for c in Clientes.listar():
            if c.email == "admin": return None
        View.cliente_inserir("admin", "admin", "0000", "1234")    
    @staticmethod
    def cliente_autenticar(email, senha):
        for c in Clientes.listar():
            if c.email == email and c.senha == senha:
                return { "id" : c.id, "nome" : c.nome }
        return None    

    @staticmethod
    def cliente_listar():
        return Clientes.listar()
    @staticmethod
    def cliente_inserir(nome, email, fone, senha):
        c = Cliente(0, nome, email, fone, senha)
        Clientes.inserir(c)
    @staticmethod
    def cliente_atualizar(id, nome, email, fone, senha):
        c = Cliente(id, nome, email, fone, senha)
        Clientes.atualizar(c)
    @staticmethod
    def cliente_excluir(id):
        c = Cliente(id, "", "", "", "")
        Clientes.excluir(c)

    @staticmethod
    def categoria_listar():
        return Categorias.listar()
    @staticmethod
    def categoria_listar_id(id):
        return Categorias.listar_id(id)
    @staticmethod
    def categoria_inserir(descricao):
        c = Categoria(0, descricao)
        Categorias.inserir(c)
    @staticmethod
    def categoria_atualizar(id, descricao):
        c = Categoria(id, descricao)
        Categorias.atualizar(c)
    @staticmethod
    def categoria_excluir(id):
        c = Categoria(id, "")
        Categorias.excluir(c)

    @staticmethod
    def produto_listar():
        return Produtos.listar()
    @staticmethod
    def produto_listar_id(id):
        for produto in Produtos.listar():
            if produto.id == id:
                return produto
        return None

    @staticmethod
    def produto_inserir(descricao, preco, estoque, id_categoria):
        c = Produto(0, descricao, preco, estoque, id_categoria)
        Produtos.inserir(c)
    @staticmethod
    def produto_atualizar(id, descricao, preco, estoque, id_categoria):
        c = Produto(id, descricao, preco, estoque, id_categoria)
        Produtos.atualizar(c)
    @staticmethod
    def produto_excluir(id):
        c = Produto(id, "", 0, 0, None)
        Produtos.excluir(c)
    @staticmethod
    def produto_reajustar(percentual):
        for obj in View.produto_listar():
            View.produto_atualizar(obj.id, obj.descricao, obj.preco * (1 + percentual), obj.estoque, obj.id_categoria)
    @staticmethod
    def venda_listar():
        return Vendas.listar()
    @staticmethod
    def venda_inserir(data, carrinho, total, idCliente):
        v = Venda(0, data, carrinho, total, idCliente)
        Vendas.inserir(v)
    @staticmethod
    def venda_atualizar(id, data, carrinho, total, idCliente):
        v = Venda(id, data, carrinho, total, idCliente)
        Vendas.atualizar(v)
    @staticmethod
    def venda_excluir(id):
        v = Venda(id, None, False, 0.0, 0)
        Vendas.excluir(v)
    @staticmethod
    def venda_item_listar():
        return VendaItems.listar()
    @staticmethod
    def venda_item_inserir(qtd, preco, idVenda, idProduto):
        vi = VendaItem(0, qtd, preco, idVenda, idProduto)
        VendaItems.inserir(vi)
    @staticmethod
    def venda_item_atualizar(id, qtd, preco, idVenda, idProduto):
        vi = VendaItem(id, qtd, preco, idVenda, idProduto)
        VendaItems.atualizar(vi)
    @staticmethod
    def venda_item_excluir(id):
        vi = VendaItem(id, 0, 0.0, 0, 0)
        VendaItems.excluir(vi)