import json

class Produto:
    def __init__(self, id, descricao, preco, estoque, id_categoria):
        self.id = id  # Atributos de instância
        self.descricao = descricao
        self.preco = preco
        self.estoque = estoque
        self.id_categoria = id_categoria

    def __str__(self):
        return f"{self.id} - {self.descricao} - Estoque: {self.estoque} - R${self.preco:.2f}"


class Produtos:
    objetos = []  # Atributo de classe

    @classmethod
    def inserir(cls, obj):
        """
        Insere um novo produto, atribuindo automaticamente um ID único.
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
        Retorna a lista completa de produtos.
        """
        cls.abrir()
        return cls.objetos[:]

    @classmethod
    def listar_id(cls, id):
        """
        Retorna o produto correspondente ao ID informado.
        """
        cls.abrir()
        return next((x for x in cls.objetos if x.id == id), None)

    @classmethod
    def atualizar(cls, obj):
        """
        Atualiza um produto existente com base no ID.
        """
        cls.abrir()
        existente = cls.listar_id(obj.id)
        if existente:
            cls.objetos.remove(existente)
            cls.objetos.append(obj)
            cls.salvar()
        else:
            raise ValueError(f"Produto com ID {obj.id} não encontrado.")

    @classmethod
    def excluir(cls, obj):
        """
        Exclui um produto existente com base no ID.
        """
        cls.abrir()
        existente = cls.listar_id(obj.id)
        if existente:
            cls.objetos.remove(existente)
            cls.salvar()
        else:
            raise ValueError(f"Produto com ID {obj.id} não encontrado.")

    @classmethod
    def salvar(cls):
        """
        Salva a lista de produtos no arquivo JSON.
        """
        with open("produtos.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default=vars)

    @classmethod
    def abrir(cls):
        """
        Carrega a lista de produtos do arquivo JSON.
        """
        cls.objetos = []
        try:
            with open("produtos.json", mode="r") as arquivo:
                objetos_json = json.load(arquivo)
                for obj in objetos_json:
                    c = Produto(
                        obj["id"],
                        obj["descricao"],
                        obj["preco"],
                        obj["estoque"],
                        obj["id_categoria"],
                    )
                    cls.objetos.append(c)
        except FileNotFoundError:
            pass
