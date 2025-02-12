import json

class Usuario:
    def __init__(self, nome, numero_matricula, endereco, tel, email, historico_emprestimos):
        self.nome = nome
        self.numero_matricula = numero_matricula
        self.endereco = endereco
        self.tel = tel
        self.email = email
        self.historico_emprestimos = historico_emprestimos
    
    def __str__(self):
        return f"{self.nome} - {self.numero_matricula} - {self.endereco} - {self.tel} - {self.email} - {self.historico_emprestimos}"

    @staticmethod
    def carregar_usuarios():
        try:
            with open('usuarios.json', 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    @staticmethod
    def salvar_usuarios(dados):
        with open('usuarios.json', 'w') as file:
            json.dump(dados, file, indent=4)

    @staticmethod
    def salvar_novo_usuario(nome, numero_matricula, endereco, tel, email, historico_emprestimos):
        usuarios = Usuario.carregar_usuarios()
        novo_usuario = {
            "nome": nome,
            "numero_matricula": numero_matricula,
            "endereco": endereco,
            "tel": tel,
            "email": email,
            "historico_emprestimos": historico_emprestimos
        }
        usuarios.append(novo_usuario)
        Usuario.salvar_usuarios(usuarios)
