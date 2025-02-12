import json
import os

class Exemplar:
    def __init__(self, descricao, situacao, data_devolucao):
        self.descricao = descricao
        self.situacao = situacao
        self.data_devolucao = data_devolucao

    def __str__(self):
        return f"{self.descricao} - {self.situacao} - {self.data_devolucao}"

    @staticmethod
    def carregar_exemplares():
        try:
            with open(os.path.join('dados', 'exemplares.json'), 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    @staticmethod
    def salvar_exemplares(dados):
        os.makedirs('dados', exist_ok=True)
        with open(os.path.join('dados', 'exemplares.json'), 'w') as file:
            json.dump(dados, file, indent=4)

    @staticmethod
    def salvar_novo_exemplar(descricao, situacao, data_devolucao):
        exemplares = Exemplar.carregar_exemplares()
        novo_exemplar = {
            "descricao": descricao,
            "situacao": situacao,
            "data_devolucao": data_devolucao
        }
        exemplares.append(novo_exemplar)
        Exemplar.salvar_exemplares(exemplares)
