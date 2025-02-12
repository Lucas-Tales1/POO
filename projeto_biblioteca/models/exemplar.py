class Exemplar:
    def __init__(self,descricao, situacao, data_devolucao):
        self.descricao = descricao
        self.situacao = situacao
        self.data_devolucao = data_devolucao

    def __str__(self):
        return f"{self.descricao} - {self.situacao} - {self.data_devolucao}"
        