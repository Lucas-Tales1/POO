import json

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