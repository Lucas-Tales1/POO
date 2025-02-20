from models.usuario import Usuario, Bibliotecario

class View:
    @staticmethod
    def usuario_bibliotecario():
        bibliotecarios = Bibliotecario.carregar_bibliotecarios()
        for b in bibliotecarios:
            if b["email"] == "admin":
                return None
        
        View.bibliotecario_inserir("admin", "0000", "Rua Admin", "000000000", "admin", "1234", "B001")

    @staticmethod
    def usuario_autenticar(email, senha):
        # Verificar tanto nos usuários quanto nos bibliotecários
        usuarios = Usuario.carregar_usuarios()
        bibliotecarios = Bibliotecario.carregar_bibliotecarios()
        
        for u in usuarios:
            if u["email"] == email and u["senha"] == senha:
                return {"id": u["id_usuario"], "nome": u["nome"], "tipo": "usuario"}
        for b in bibliotecarios:
            if b["email"] == email and b["senha"] == senha:
                return {"id": b["numero_matricula"], "nome": b["nome"], "tipo": "bibliotecario"}
        return None

    @staticmethod
    def usuario_inserir(nome, numero_matricula, endereco, tel, email, senha, historico_emprestimos=[]):
        if View.email_existe(email):
            print("Erro: Email já está em uso.")
            return
        else:
            id_usuario = View.proximo_id()
            Usuario.salvar_novo_usuario(id_usuario, nome, numero_matricula, endereco, tel, email, senha, historico_emprestimos)

    @staticmethod
    def bibliotecario_inserir(nome, numero_matricula, endereco, tel, email, senha, id_bibliotecario):
        Bibliotecario.salvar_novo_bibliotecario(nome, numero_matricula, endereco, tel, email, senha, id_bibliotecario)

    @staticmethod
    def usuario_logout(session):
        session.clear()

    @staticmethod
    def proximo_id():
        usuarios = Usuario.carregar_usuarios()
        if not usuarios:
            return 1
        else:
            ultimo_usuario = usuarios[-1]
            return ultimo_usuario["id_usuario"] + 1

    @staticmethod
    def email_existe(email):
        usuarios = Usuario.carregar_usuarios()
        for u in usuarios:
            if u["email"] == email:
                return True
        return False

View.usuario_bibliotecario()
