import json

class Cliente:
    def __init__(self, id, nome, email, fone, senha):
        self.id = id
        self.nome = nome
        self.email = email
        self.fone = fone
        self.senha = senha

    def __str__(self):
        return f"{self.id} - {self.nome} - {self.email} - {self.fone}"

class Clientes:
    objetos = []

    @classmethod
    def inserir(cls, obj):
        cls.objetos.append(obj)
        cls.salvar()

    @classmethod
    def listar(cls):
        return cls.objetos

    @classmethod
    def salvar(cls):
        with open("clientes.json", "w") as f:
            json.dump([obj.__dict__ for obj in cls.objetos], f)

    @classmethod
    def abrir(cls):
        try:
            with open("clientes.json", "r") as f:
                clientes_data = json.load(f)
                cls.objetos = [Cliente(c["id"], c["nome"], c["email"], c["fone"], c["senha"]) for c in clientes_data]
        except FileNotFoundError:
            cls.objetos = []
