import json
from datetime import datetime

class Venda:
    def __init__(self,id,data,carrinho,total,idCliente):
        self.id = id
        self.data = data
        self.carrinho = carrinho
        self.total = total 
        self.idCliente = idCliente
    def __str__(self): 
        return f'id = {self.id} / Data = {self.data} / Carrinho = {self.carrinho} / Total = {self.total} / idCliente = {self.idCliente}'
    
class Vendas:
    objetos = []
    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        id = 0
        for x in cls.objetos:
            if x.id > id:
                id = x.id
        obj.id = id + 1
        cls.objetos.append(obj)
        cls.salvar()
    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.objetos[:]
    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for x in cls.objetos:
            if x.id == id:
                return x
        return None
    @classmethod
    def atualizar(cls, obj):
        x = cls.listar_id(obj.id)
        if x is not None:
            cls.objetos.remove(x)
            cls.objetos.append(obj)
            cls.salvar()
    @classmethod
    def excluir(cls, obj):
        x = cls.listar_id(obj.id)
        if x is not None:
            cls.objetos.remove(x)
            cls.salvar()
    @classmethod
    def salvar(cls):
        with open("vendas.json", mode="w") as arquivo:
            if cls.objetos:
                try:
                    json.dump(cls.objetos, arquivo, default=lambda o: {
                        'id': o.id,
                        'data': o.data if isinstance(o.data, str) else o.data.strftime('%Y-%m-%d %H:%M:%S'), 
                        'carrinho': o.carrinho,
                        'total': o.total,
                        'idCliente': o.idCliente
                    })
                    print("Dados salvos com sucesso.")
                except Exception as e:
                    print(f"Erro ao salvar dados: {e}")
            else:
                arquivo.write('[]')
                print("Arquivo JSON salvo vazio.")
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("vendas.json", mode="r") as arquivo:
                try:
                    conteudo = arquivo.read().strip()
                    if not conteudo:
                        print("Arquivo JSON vazio.")
                        return
                    objetos_json = json.loads(conteudo)
                    for obj in objetos_json:
                        try:
                            data = datetime.strptime(obj["data"], '%Y-%m-%d %H:%M:%S')
                        except ValueError:
                            data = datetime.strptime(obj["data"], '%Y-%m-%d')
                        v = Venda(obj["id"], data, obj["carrinho"], obj["total"], obj["idCliente"])
                        cls.objetos.append(v)
                    print("Dados carregados com sucesso.")
                except json.JSONDecodeError as e:
                    print(f"Erro ao decodificar JSON: {e}")
        except FileNotFoundError:
            with open("vendas.json", mode="w") as arquivo:
                arquivo.write('[]')
                print("Arquivo vendas.json criado. Nenhum dado carregado.")
        except Exception as e:
            print(f"Erro ao abrir arquivo: {e}")


   