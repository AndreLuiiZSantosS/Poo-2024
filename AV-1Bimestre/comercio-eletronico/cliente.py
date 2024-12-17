import json

class Cliente:
    def __init__(self, id, nome, email, fone, senha):
        self.id = id  # Atributo de instância
        self.nome = nome
        self.email = email
        self.fone = fone
        self.senha = senha

    def __str__(self):
        return f"{self.id} - {self.nome} - {self.email} - {self.fone}"


class Clientes:
    objetos = []  # Atributo de classe

    @classmethod
    def inserir(cls, obj):
        """
        Insere um novo cliente, atribuindo automaticamente um ID único.
        """
        cls.abrir()
        # Calcula o próximo ID disponível
        id = max((x.id for x in cls.objetos), default=0) + 1
        obj.id = id
        cls.objetos.append(obj)
        cls.salvar()

    @classmethod
    def listar(cls):
        """
        Retorna a lista completa de clientes.
        """
        cls.abrir()
        return cls.objetos

    @classmethod
    def listar_id(cls, id):
        """
        Retorna o cliente correspondente ao ID informado.
        """
        cls.abrir()
        return next((x for x in cls.objetos if x.id == id), None)

    @classmethod
    def atualizar(cls, obj):
        """
        Atualiza um cliente existente com base no ID.
        """
        cls.abrir()
        existente = cls.listar_id(obj.id)
        if existente:
            cls.objetos.remove(existente)
            cls.objetos.append(obj)
            cls.salvar()
        else:
            raise ValueError(f"Cliente com ID {obj.id} não encontrado.")

    @classmethod
    def excluir(cls, obj):
        """
        Exclui um cliente existente com base no ID.
        """
        cls.abrir()
        existente = cls.listar_id(obj.id)
        if existente:
            cls.objetos.remove(existente)
            cls.salvar()
        else:
            raise ValueError(f"Cliente com ID {obj.id} não encontrado.")

    @classmethod
    def salvar(cls):
        """
        Salva a lista de clientes no arquivo JSON.
        """
        with open("clientes.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default=vars)

    @classmethod
    def abrir(cls):
        """
        Carrega a lista de clientes do arquivo JSON.
        """
        cls.objetos = []
        try:
            with open("clientes.json", mode="r") as arquivo:
                clientes_json = json.load(arquivo)
                for obj in clientes_json:
                    c = Cliente(obj["id"], obj["nome"], obj["email"], obj["fone"], obj["senha"])
                    cls.objetos.append(c)
        except FileNotFoundError:
            pass
