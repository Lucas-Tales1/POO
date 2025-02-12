import json

class Bibliotecario:
    def __init__(self,nome,id):
        self.nome = nome
        self.id = id
    
    def __str__(self):
        return f"{self.nome} - {self.id}"