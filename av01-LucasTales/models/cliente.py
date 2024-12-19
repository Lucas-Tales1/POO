import json
from models.carrinho import Carrinho

class Cliente:
    def __init__(self, id, nome, email, fone, senha):
        self.id = id 
        self.nome = nome
        self.email = email
        self.fone = fone
        self.senha = senha
        self.carrinho = Carrinho()

    def __str__(self):
        return f"{self.id} - {self.nome} - {self.email} - {self.fone}"


class Clientes:
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
        return cls.objetos

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
        with open("clientes.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default=lambda o: {
                'id': o.id,
                'nome': o.nome,
                'email': o.email,
                'fone': o.fone,
                'senha': o.senha,
                'carrinho': o.carrinho.salvar()
            })

    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("clientes.json", mode="r") as arquivo:
                try:
                    clientes_json = json.load(arquivo)
                    for obj in clientes_json:
                        c = Cliente(obj["id"], obj["nome"], obj["email"], obj["fone"], obj["senha"])
                        c.carrinho.abrir(obj.get("carrinho", []))
                        cls.objetos.append(c)
                except json.JSONDecodeError as e:
                    print(f"Erro ao decodificar JSON: {e}")
                    cls.objetos = []
        except FileNotFoundError:
            with open("clientes.json", mode="w") as arquivo:
                arquivo.write("[]")
                print("Arquivo clientes.json criado.")
        except Exception as e:
            print(f"Erro ao abrir arquivo: {e}")

