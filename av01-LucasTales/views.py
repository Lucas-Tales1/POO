from models.cliente import Cliente, Clientes
from models.carrinho import Carrinho
from models.categoria import Categoria, Categorias
from models.produto import Produto, Produtos
from models.venda import Venda, Vendas
from models.vendaItem import VendaItem, VendaItems

class View:
    @staticmethod
    def cliente_admin():
        for c in Clientes.listar():
            if c.email == "admin":
                return None
        View.cliente_inserir("admin", "admin", "0000", "1234")

    @staticmethod
    def cliente_autenticar(email, senha):
        for c in Clientes.listar():
            if c.email == email and c.senha == senha:
                return {"id": c.id, "nome": c.nome}
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
    def listar_id_cliente(id_cliente):
        return Clientes.listar_id(id_cliente)

    @staticmethod
    def atualizar_cliente(cliente):
        return Clientes.atualizar(cliente)

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

    @classmethod
    def cliente_adicionar_produto(cls):
        if cls.cliente_autenticado:
            cls.cliente_listar_produto()
            id_produto = int(input("\nInforme o ID do produto a adicionar: "))
            qtd = int(input("Informe a quantidade: "))
            produto = View.produto_listar_id(id_produto)
            if produto:
                try:
                    View.diminuir_estoque(id_produto, qtd)
                    # Adicionando o produto ao carrinho do cliente autenticado
                    cliente = Clientes.listar_id(cls.cliente_autenticado["id"])
                    if cliente:
                        cliente.carrinho.inserir(produto, qtd)  # Usar o método inserir
                        Clientes.atualizar(cliente)
                        print("\nProduto adicionado ao carrinho com sucesso!")
                    else:
                        print("\nCliente não encontrado!")
                except ValueError as e:
                    print(f"\nErro: {e}")
            else:
                print("\nProduto não encontrado!")
        else:
            print("Por favor, autentique-se primeiro.")

    @staticmethod
    def adicionar_produto_carrinho(id_cliente, id_produto, quantidade):
        cliente = Clientes.listar_id(id_cliente)
        if cliente:
            produto = View.produto_listar_id(id_produto)
            if produto:
                try:
                    View.diminuir_estoque(id_produto, quantidade)
                    cliente.carrinho.inserir(produto, quantidade)
                    Produtos.atualizar(produto)
                    Clientes.atualizar(cliente)
                    print(f"Adicionado {quantidade} de {produto.descricao} ao carrinho do cliente {cliente.nome}.")
                except ValueError as e:
                    print(e)
            else:
                print(f"Produto com ID {id_produto} não encontrado.")
        else:
            print(f"Cliente com ID {id_cliente} não encontrado.")   

    @staticmethod
    def diminuir_estoque(id_produto, quantidade):
        Produtos.diminuir_estoque(id_produto, quantidade)


    @staticmethod
    def remover_produto_carrinho(id_cliente, id_produto):
        cliente = Clientes.listar_id(id_cliente)
        if cliente:
            cliente.carrinho.remover_item(id_produto)
            Clientes.atualizar(cliente)
            print("\nProduto removido do carrinho com sucesso!")
        else:
            print(f"Cliente com ID {id_cliente} não encontrado.")   

    @staticmethod
    def cliente_fechar_pedido(cliente_id):
        cliente = Clientes.listar_id(cliente_id)
        if cliente:
            itens = cliente.carrinho.listar_itens()
            total = sum(item[0].preco * item[1] for item in itens)
            if total > 0:
                data = input("Informe a data para finalizar o pedido (YYYY-MM-DD): ")
                View.venda_inserir(data, False, total, cliente_id)
                print("\nPedido fechado com sucesso!")
                cliente.carrinho.esvaziar()
                Clientes.atualizar(cliente)
            else:
                print("\nNenhum item no carrinho para fechar o pedido!")
        else:
            print("Cliente não encontrado.")


    @staticmethod
    def visualizar_carrinho(id_cliente):
        cliente = Clientes.listar_id(id_cliente)
        if cliente:
            if cliente.carrinho.listar_itens():
                print("\n--- Itens no Carrinho ---")
                for produto, quantidade in cliente.carrinho.listar_itens():
                    print(f"Produto: {produto.descricao}, Quantidade: {quantidade}, Preço Unitário: R${produto.preco:.2f}")
            else:
                print("\nO carrinho está vazio.")
        else:
            print(f"Cliente com ID {id_cliente} não encontrado.")
