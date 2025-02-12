class Livro:
    def __init__(self,id,titulo,autor,genero,num_paginas,ano_publicacao,disponibilidade,qtd_total,qtd_disponivel):
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
        