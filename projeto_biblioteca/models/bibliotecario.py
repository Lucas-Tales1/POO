import json
import os

class Bibliotecario:
    def __init__(self, nome, id):
        self.nome = nome
        self.id = id
    
    def __str__(self):
        return f"{self.nome} - {self.id}"

    @staticmethod
    def carregar_bibliotecarios():
        try:
            with open('bibliotecarios.json', 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    @staticmethod
    def salvar_bibliotecarios(dados):
        with open('bibliotecarios.json', 'w') as file:
            json.dump(dados, file, indent=4)

    @staticmethod
    def salvar_novo_bibliotecario(nome, id):
        bibliotecarios = Bibliotecario.carregar_bibliotecarios()
        novo_bibliotecario = {
            "nome": nome,
            "id": id
        }
        bibliotecarios.append(novo_bibliotecario)
        Bibliotecario.salvar_bibliotecarios(bibliotecarios)
