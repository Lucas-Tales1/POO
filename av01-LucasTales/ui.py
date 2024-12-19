from views import View

class UI:
    cliente_id = 0
    cliente_nome = ""
    cliente_autenticado = None  # Inicializa o cliente autenticado

    @staticmethod
    def menu_visitante():
        print("1 - Abrir conta, 2 - Entrar no Sistema, 99 - Fim")
        op = int(input("\nInforme uma opção: "))
        if op == 1:
            UI.visitante_abrir_conta()
        if op == 2:
            UI.visitante_entrar_no_sistema()
        return op

    @staticmethod
    def menu_admin():
        print("Cadastro de Clientes")
        print("  1 - Inserir, 2 - Listar, 3 - Atualizar, 4 - Excluir")
        print("Cadastro de Categorias")
        print("  5 - Inserir, 6 - Listar, 7 - Atualizar, 8 - Excluir")
        print("Cadastro de Produtos")
        print("  9 - Inserir, 10 - Listar, 11 - Atualizar, 12 - Excluir, 13 - Reajustar")
        print("Ver Pedidos")
        print("14 - Ver Pedidos")
        print("0 - Sair, 99 - Fim")
        op = int(input("\nInforme uma opção: "))
        if op == 0:
            UI.sair_do_sistema()

        if op == 1:
            UI.cliente_inserir()
        if op == 2:
            UI.cliente_listar()
        if op == 3:
            UI.cliente_atualizar()
        if op == 4:
            UI.cliente_excluir()

        if op == 5:
            UI.categoria_inserir()
        if op == 6:
            UI.categoria_listar()
        if op == 7:
            UI.categoria_atualizar()
        if op == 8:
            UI.categoria_excluir()

        if op == 9:
            UI.produto_inserir()
        if op == 10:
            UI.produto_listar()
        if op == 11:
            UI.produto_atualizar()
        if op == 12:
            UI.produto_excluir()
        if op == 13:
            UI.produto_reajustar()

        if op == 14:
            UI.ver_pedidos()

        return op

    @staticmethod
    def menu_cliente():
        print("1 - Listar Produtos, 2 - Adicionar Produto no Carrinho, 3 - Ver meu carrinho, 4 - Retirar produto do carrinho, 5 - Finalizar pedido, 6 - Ver Meus Pedidos")
        print("0 - Sair, 99 - Fim")
        op = int(input("\nInforme uma opção: "))
        if op == 0:
            UI.sair_do_sistema()
        if op == 1:
            UI.cliente_listar_produto()
        if op == 2:
            UI.cliente_adicionar_produto()
        if op == 3:
            UI.cliente_visualizar_carrinho()
        if op == 4:
            UI.cliente_remover_produto_carrinho()
        if op == 5:
            UI.cliente_fechar_pedido()
        if op == 6:
            UI.cliente_meus_pedidos()
        return op

    @classmethod
    def main(cls):
        View.cliente_admin()
        op = 0
        while op != 99:
            if cls.cliente_id == 0:
                op = UI.menu_visitante()
            else:
                admin = cls.cliente_nome == "admin"
                print("Bem-vindo(a), " + cls.cliente_nome)
                if admin:
                    op = UI.menu_admin()
                else:
                    op = UI.menu_cliente()

    @classmethod
    def visitante_abrir_conta(cls):
        cls.cliente_inserir()

    @classmethod
    def visitante_entrar_no_sistema(cls):
        email = input("Informe o email: ")
        senha = input("Informe a senha: ")
        obj = View.cliente_autenticar(email, senha)
        cls.cliente_autenticado = obj
        if obj is None:
            print("E-mail ou senha inválidos")
        else:
            cls.cliente_id = obj["id"]
            cls.cliente_nome = obj["nome"]

    @classmethod
    def sair_do_sistema(cls):
        cls.cliente_id = 0
        cls.cliente_nome = ""
        cls.cliente_autenticado = None

    @classmethod
    def cliente_inserir(cls):
        nome = input("Informe o nome: ")
        email = input("Informe o email: ")
        fone = input("Informe o fone: ")
        senha = input("Informe a senha: ")
        View.cliente_inserir(nome, email, fone, senha)

    @classmethod
    def cliente_listar(cls):
        clientes = View.cliente_listar()
        if len(clientes) == 0:
            print("Nenhum cliente cadastrado")
        else:
            for cliente in clientes:
                print(cliente)

    @classmethod
    def cliente_atualizar(cls):
        cls.cliente_listar()
        id = int(input("Informe o id do cliente a ser alterado: "))
        nome = input("Informe o novo nome: ")
        email = input("Informe o novo email: ")
        fone = input("Informe o novo fone: ")
        senha = input("Informe a senha: ")
        View.cliente_atualizar(id, nome, email, fone, senha)

    @classmethod
    def cliente_excluir(cls):
        cls.cliente_listar()
        id = int(input("Informe o id do cliente a ser excluído: "))
        View.cliente_excluir(id)

    @classmethod
    def categoria_inserir(cls):
        desc = input("Informe a descrição: ")
        View.categoria_inserir(desc)

    @classmethod
    def categoria_listar(cls):
        objetos = View.categoria_listar()
        if len(objetos) == 0:
            print("Nenhuma categoria cadastrada")
        else:
            for obj in objetos:
                print(obj)

    @classmethod
    def categoria_atualizar(cls):
        cls.categoria_listar()
        id = int(input("Informe o id da categoria a ser alterada: "))
        desc = input("Informe a nova descrição: ")
        View.categoria_atualizar(id, desc)

    @classmethod
    def categoria_excluir(cls):
        cls.categoria_listar()
        id = int(input("Informe o id da categoria a ser excluída: "))
        View.categoria_excluir(id)

    @classmethod
    def produto_inserir(cls):
        desc = input("Informe a descrição: ")
        prc = float(input("Informe o preço: "))
        est = int(input("Informe o estoque: "))
        UI.categoria_listar()
        id_categoria = int(input("Informe o id da categoria: "))
        View.produto_inserir(desc, prc, est, id_categoria)

    @classmethod
    def produto_listar(cls):
        objetos = View.produto_listar()
        if len(objetos) == 0:
            print("Nenhum produto cadastrado")
        else:
            for obj in objetos:
                id_categoria = obj.id_categoria
                categoria = View.categoria_listar_id(id_categoria)
                print(f"{obj} - {categoria.descricao}")

    @classmethod
    def produto_atualizar(cls):
        cls.produto_listar()
        id = int(input("Informe o id do produto a ser alterado: "))
        desc = input("Informe a nova descrição: ")
        prc = float(input("Informe o novo preço: "))
        est = int(input("Informe o novo estoque: "))
        UI.categoria_listar()
        id_categoria = int(input("Informe o id da categoria: "))
        View.produto_atualizar(id, desc, prc, est, id_categoria)

    @classmethod
    def produto_excluir(cls):
        cls.produto_listar()
        id = int(input("Informe o id do produto a ser excluído: "))
        View.produto_excluir(id)

    @classmethod
    def produto_reajustar(cls):
        reajuste = float(input("Informe o percentual de reajuste em %: "))
        View.produto_reajustar(reajuste / 100)

    @classmethod
    def cliente_listar_produto(cls):
        produtos = View.produto_listar()
        if len(produtos) == 0:
            print("\nNenhum produto disponível\n")
        else:
            for produto in produtos:
                id_categoria = produto.id_categoria
                categoria = View.categoria_listar_id(id_categoria)
                if categoria:
                    print(f"{produto} - {categoria.descricao}")
                else:
                    print(f"{produto} - Categoria não encontrada")

    @classmethod
    def cliente_adicionar_produto(cls):
        if cls.cliente_autenticado:
            cls.cliente_listar_produto()
            id_produto = int(input("\nInforme o ID do produto a adicionar: "))
            qtd = int(input("Informe a quantidade: "))
            View.adicionar_produto_carrinho(cls.cliente_autenticado["id"], id_produto, qtd)

    @classmethod
    def cliente_visualizar_carrinho(cls):
        if cls.cliente_autenticado:
            View.visualizar_carrinho(cls.cliente_autenticado["id"])
    
    @classmethod
    def cliente_remover_produto_carrinho(cls):
        if cls.cliente_autenticado:
            id_produto = int(input("Informe o ID do produto a remover: "))
            View.remover_produto_carrinho(cls.cliente_autenticado["id"], id_produto)

    @classmethod
    def cliente_fechar_pedido(cls):
        if cls.cliente_autenticado:
            View.cliente_fechar_pedido(cls.cliente_autenticado["id"])

    @classmethod
    def cliente_meus_pedidos(cls):
        vendas = View.venda_listar()
        encontrou_pedidos = False
        for venda in vendas:
            if venda.idCliente == cls.cliente_id:
                print(venda)
                encontrou_pedidos = True
        if not encontrou_pedidos:
            print("\nVocê não possui pedidos!")

    @classmethod
    def venda_inserir(cls):
        data = input("Informe a data (YYYY-MM-DD): ")
        carrinho = input("Está no carrinho (True/False)? ").lower() == 'true'
        total = float(input("Informe o total da venda: "))
        idCliente = int(input("Informe o ID do cliente: "))
        View.venda_inserir(data, carrinho, total, idCliente)

    @classmethod
    def venda_listar(cls):
        vendas = View.venda_listar()
        if len(vendas) == 0:
            print("Nenhuma venda cadastrada")
        else:
            for venda in vendas:
                print(venda)

    @classmethod
    def venda_atualizar(cls):
        cls.venda_listar()
        id = int(input("Informe o id da venda a ser alterada: "))
        data = input("Informe a nova data (YYYY-MM-DD): ")
        carrinho = input("Está no carrinho (True/False)? ").lower() == 'true'
        total = float(input("Informe o novo total da venda: "))
        idCliente = int(input("Informe o ID do cliente: "))
        View.venda_atualizar(id, data, carrinho, total, idCliente)

    @classmethod
    def venda_excluir(cls):
        cls.venda_listar()
        id = int(input("Informe o id da venda a ser excluída: "))
        View.venda_excluir(id)

    @classmethod
    def venda_item_inserir(cls):
        qtd = int(input("Informe a quantidade do produto: "))
        preco = float(input("Informe o preço do produto: "))
        idVenda = int(input("Informe o ID da venda: "))
        idProduto = int(input("Informe o ID do produto: "))
        View.venda_item_inserir(qtd, preco, idVenda, idProduto)

    @classmethod
    def venda_item_listar(cls):
        itens = View.venda_item_listar()
        if len(itens) == 0:
            print("Nenhum item de venda cadastrado")
        else:
            for item in itens:
                print(item)

    @classmethod
    def venda_item_atualizar(cls):
        cls.venda_item_listar()
        id = int(input("Informe o id do item de venda a ser alterado: "))
        qtd = int(input("Informe a nova quantidade do produto: "))
        preco = float(input("Informe o novo preço do produto: "))
        idVenda = int(input("Informe o ID da venda: "))
        idProduto = int(input("Informe o ID do produto: "))
        View.venda_item_atualizar(id, qtd, preco, idVenda, idProduto)

    @classmethod
    def venda_item_excluir(cls):
        cls.venda_item_listar()
        id = int(input("Informe o id do item de venda a ser excluído: "))
        View.venda_item_excluir(id)
                        
    @classmethod
    def ver_pedidos(cls):
        vendas = View.venda_listar()
        if len(vendas) == 0:
            print("Nenhum pedido encontrado")
        else:
            for venda in vendas:
                print(venda)

UI.main() 