import json
from livro import Livro

class Emprestimo:
    def __init__(self, livro, usuario, data_emprestimo, data_devolucao, data_devolucao_real, id):
        self.livro = livro
        self.usuario = usuario
        self.data_emprestimo = data_emprestimo
        self.data_devolucao = data_devolucao
        self.data_devolucao_real = data_devolucao_real
        self.id = id

    def __str__(self):
        return f"{self.livro} - {self.usuario} - {self.data_emprestimo} - {self.data_devolucao} - {self.data_devolucao_real} - {self.id}"

    @staticmethod
    def carregar_emprestimos():
        try:
            with open('emprestimos.json', 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    @staticmethod
    def salvar_emprestimos(dados):
        with open('emprestimos.json', 'w') as file:
            json.dump(dados, file, indent=4)

    @staticmethod
    def salvar_novo_emprestimo(livro, usuario, data_emprestimo, data_devolucao, data_devolucao_real, id):
        emprestimos = Emprestimo.carregar_emprestimos()
        novo_emprestimo = {
            "livro": livro,
            "usuario": usuario,
            "data_emprestimo": data_emprestimo,
            "data_devolucao": data_devolucao,
            "data_devolucao_real": data_devolucao_real,
            "id": id
        }
        emprestimos.append(novo_emprestimo)
        Emprestimo.salvar_emprestimos(emprestimos)
