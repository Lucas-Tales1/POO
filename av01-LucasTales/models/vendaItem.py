import json

class VendaItem:
    def __init__(self,id,qtd,preco,idVenda,idProduto):
        self.id = id
        self.qtd = qtd
        self.preco = preco
        self.idVenda = idVenda
        self.idProduto = idProduto
    def __str__(self): 
        return f'id = {self.id} / quantidade = {self.qtd} / preço = {self.preco} / idVenda = {self.idVenda} / idProduto = {self.idProduto}'

class VendaItems:
    objetos = []

    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        id = 0
        for x in cls.objetos:
            if x.id > id: id = x.id
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
            if x.id == id: return x
        return None

    @classmethod
    def atualizar(cls, obj):
        x = cls.listar_id(obj.id)
        if x != None:
            cls.objetos.remove(x)
            cls.objetos.append(obj)
            cls.salvar()

    @classmethod
    def excluir(cls, obj):
        x = cls.listar_id(obj.id)
        if x != None:
            cls.objetos.remove(x)
            cls.salvar()

    @classmethod
    def salvar(cls):
        with open("vendaItems.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default=vars)

    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("vendaItems.json", mode="r") as arquivo:
                objetos_json = json.load(arquivo)
                for obj in objetos_json:
                    c = VendaItem(obj["id"], obj["qtd"], obj["preco"], obj["idVenda"], obj["idProduto"])
                    cls.objetos.append(c)
        except FileNotFoundError:
            pass
