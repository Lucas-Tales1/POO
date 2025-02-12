import json

class Usuario:
    def __init__(self, nome, numero_matricula,endereco,tel,email,historico_emprestimos):
        self.nome = nome
        self.numero_matricula = numero_matricula
        self.endereco = endereco
        self.tel = tel
        self.email = email
        self.historico_emprestimos = historico_emprestimos
    
    def __str__(self):
        return f"{self.nome} - {self.numero_matricula} - {self.endereco} - {self.tel} - {self.email} - {self.historico_emprestimos}"