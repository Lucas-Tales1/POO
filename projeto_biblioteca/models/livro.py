import json
import os

class Livro:
    def __init__(self, id, titulo, autor, genero, num_paginas, ano_publicacao, disponibilidade, qtd_total, qtd_disponivel):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.num_paginas = num_paginas
        self.ano_publicacao = ano_publicacao
        self.disponibilidade = disponibilidade
        self.qtd_total = qtd_total
        self.qtd_disponivel = qtd_disponivel
    
    def __str__(self):
        return f"{self.id} - {self.titulo} - {self.autor} - {self.genero} - {self.num_paginas} - {self.ano_publicacao} - {self.disponibilidade} - {self.qtd_total} - {self.qtd_disponivel}"

    @staticmethod
    def carregar_livros():
        try:
            with open(os.path.join('dados', 'livros.json'), 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    @staticmethod
    def salvar_livros(dados):
        os.makedirs('dados', exist_ok=True)
        with open(os.path.join('dados', 'livros.json'), 'w') as file:
            json.dump(dados, file, indent=4)

    @staticmethod
    def salvar_novo_livro(id, titulo, autor, genero, num_paginas, ano_publicacao, disponibilidade, qtd_total, qtd_disponivel):
        livros = Livro.carregar_livros()
        novo_livro = {
            "id": id,
            "titulo": titulo,
            "autor": autor,
            "genero": genero,
            "num_paginas": num_paginas,
            "ano_publicacao": ano_publicacao,
            "disponibilidade": disponibilidade,
            "qtd_total": qtd_total,
            "qtd_disponivel": qtd_disponivel
        }
        livros.append(novo_livro)
        Livro.salvar_livros(livros)
