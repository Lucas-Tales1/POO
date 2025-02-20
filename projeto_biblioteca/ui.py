from views import View

class UI:
    usuario_id = 0
    usuario_nome = ""
    usuario_autenticado = None  

    @classmethod
    def main(cls):
        View.usuario_bibliotecario()
        op = 0
        while op != 99:
            if cls.usuario_id == 0:
                op = UI.menu_visitante()
            else:
                bibliotecario = cls.usuario_nome == "admin"
                print("Bem-vindo(a), " + cls.usuario_nome)
                if bibliotecario:
                    op = UI.menu_bibliotecario()
                else:
                    op = UI.menu_usuario()
            if op == 99:
                cls.sair_do_sistema()

    @staticmethod
    def menu_visitante():
        print("1 - Abrir conta, 2 - Entrar no Sistema, 99 - Fim")
        op = int(input("\nInforme uma opção: "))
        if op == 1:
            UI.visitante_abrir_conta()
        if op == 2:
            UI.visitante_entrar_no_sistema()
        if op == 99:
            UI.sair_do_sistema()
        return op

    @staticmethod
    def menu_bibliotecario():
        print("Cadastro de usuários")
        print("  1 - Registrar, 2 - Listar, 3 - Atualizar, 4 - Excluir")
        print("Cadastro de Livros")
        print("  5 - Adicionar, 6 - Listar, 7 - Atualizar, 8 - Excluir")
        print("Cadastro de exemplares")
        print("  9 - Adicionar, 10 - Listar, 11 - Atualizar, 12 - Excluir")
        print("Gerenciar Empréstimos")
        print(" 13 - Listar")
        print("0 - Sair, 99 - Fim")
        op = int(input("\nInforme uma opção: "))
        if op == 0:
            UI.sair_da_conta()
        if op == 99:
            UI.sair_do_sistema()
        if(op != 0 and op != 99):
            print("Funções de usuário ainda não implementadas")

    @staticmethod
    def menu_usuario():
        print("1 - Listar livros, 2 - Buscar livro, 3 - Fazer empréstimo, 4 - Devolver livro, 5 - Histórico de Empréstimos")
        print("0 - Sair, 99 - Fim")
        op = int(input("\nInforme uma opção: "))
        if op == 0:
            UI.sair_da_conta()
        if op == 99:
            UI.sair_do_sistema()
        if(op != 0 and op != 99):
            print("Funções de usuário ainda não implementadas")

    @staticmethod
    def visitante_abrir_conta():
        nome = input("Nome: ")
        numero_matricula = input("Número de Matrícula: ")
        endereco = input("Endereço: ")
        tel = input("Telefone: ")
        email = input("Email: ")
        senha = input("Senha: ")
        tipo = input("Tipo (1 - Usuário, 2 - Bibliotecário): ")

        if tipo == "1":
            View.usuario_inserir(nome, numero_matricula, endereco, tel, email, senha)
        elif tipo == "2":
            id_bibliotecario = input("ID Bibliotecário: ")
            View.bibliotecario_inserir(nome, numero_matricula, endereco, tel, email, senha, id_bibliotecario)
        else:
            print("Tipo inválido.")

    @staticmethod
    def visitante_entrar_no_sistema():
        email = input("Email: ")
        senha = input("Senha: ")
        usuario = View.usuario_autenticar(email, senha)

        if usuario:
            UI.usuario_id = usuario["id"]
            UI.usuario_nome = usuario["nome"]
            UI.usuario_autenticado = usuario["tipo"]
            print(f"Bem-vindo, {UI.usuario_nome}!")

            if UI.usuario_autenticado == "bibliotecario":
                UI.menu_bibliotecario()
            elif UI.usuario_autenticado == "usuario":
                UI.menu_usuario()
        else:
            print("Email ou senha incorretos.")

    @staticmethod
    def sair_da_conta():
        print("Saindo da conta...")
        UI.usuario_id = 0
        UI.usuario_nome = ""
        UI.usuario_autenticado = None
        View.usuario_logout(session={})
    
    def sair_do_sistema():
        print("Saindo do sistema...")
        exit()
        

UI.main()
