import json
import os

class Usuario:
    def __init__(self, id_usuario, nome, numero_matricula, endereco, tel, email, senha, historico_emprestimos):
        self.id_usuario = id_usuario
        self.nome = nome
        self.numero_matricula = numero_matricula
        self.endereco = endereco
        self.tel = tel
        self.email = email
        self.senha = senha
        self.historico_emprestimos = historico_emprestimos
    
    def __str__(self):
        return f"{self.id_usuario} - {self.nome} - {self.numero_matricula} - {self.endereco} - {self.tel} - {self.email} - {self.historico_emprestimos}"

    @staticmethod
    def carregar_usuarios():
        try:
            with open(os.path.join('dados', 'usuarios.json'), 'r') as file:
                try:
                    return json.load(file)
                except json.JSONDecodeError:
                    return []
        except FileNotFoundError:
            return []

    @staticmethod
    def salvar_usuarios(dados):
        os.makedirs('dados', exist_ok=True)
        with open(os.path.join('dados', 'usuarios.json'), 'w') as file:
            json.dump(dados, file, indent=4)

    @staticmethod
    def salvar_novo_usuario(id_usuario, nome, numero_matricula, endereco, tel, email, senha, historico_emprestimos):
        usuarios = Usuario.carregar_usuarios()
        novo_usuario = {
            "id_usuario": id_usuario,
            "nome": nome,
            "numero_matricula": numero_matricula,
            "endereco": endereco,
            "tel": tel,
            "email": email,
            "senha": senha,
            "historico_emprestimos": historico_emprestimos
        }
        usuarios.append(novo_usuario)
        Usuario.salvar_usuarios(usuarios)

class Bibliotecario(Usuario):
    def __init__(self, nome, numero_matricula, endereco, tel, email, senha, id_bibliotecario):
        super().__init__(None, nome, numero_matricula, endereco, tel, email, senha, historico_emprestimos=[])
        self.id_bibliotecario = id_bibliotecario
    
    def __str__(self):
        return f"{self.nome} - {self.numero_matricula} - {self.endereco} - {self.tel} - {self.email} - {self.id_bibliotecario}"
    
    @staticmethod
    def carregar_bibliotecarios():
        try:
            with open(os.path.join('dados', 'bibliotecarios.json'), 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    @staticmethod
    def salvar_bibliotecarios(dados):
        os.makedirs('dados', exist_ok=True)
        with open(os.path.join('dados', 'bibliotecarios.json'), 'w') as file:
            json.dump(dados, file, indent=4)

    @staticmethod
    def salvar_novo_bibliotecario(nome, numero_matricula, endereco, tel, email, senha, id_bibliotecario):
        bibliotecarios = Bibliotecario.carregar_bibliotecarios()
        novo_bibliotecario = {
            "nome": nome,
            "numero_matricula": numero_matricula,
            "endereco": endereco,
            "tel": tel,
            "email": email,
            "senha": senha,
            "id_bibliotecario": id_bibliotecario
        }
        bibliotecarios.append(novo_bibliotecario)
        Bibliotecario.salvar_bibliotecarios(bibliotecarios)
