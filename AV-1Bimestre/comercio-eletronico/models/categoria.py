import json

class Categoria:
    def __init__(self, id, descricao):
        self.id = id  # Atributo de instância
        self.descricao = descricao

    def __str__(self):
        return f"{self.id} - {self.descricao}"


class Categorias:
    objetos = []  # Atributo de classe

    @classmethod
    def inserir(cls, obj):
        """
        Insere uma nova categoria, atribuindo automaticamente um ID único.
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
        Retorna a lista completa de categorias.
        """
        cls.abrir()
        return cls.objetos

    @classmethod
    def listar_id(cls, id):
        """
        Retorna a categoria correspondente ao ID informado.
        """
        cls.abrir()
        return next((x for x in cls.objetos if x.id == id), None)

    @classmethod
    def atualizar(cls, obj):
        """
        Atualiza uma categoria existente com base no ID.
        """
        cls.abrir()
        existente = cls.listar_id(obj.id)
        if existente:
            cls.objetos.remove(existente)
            cls.objetos.append(obj)
            cls.salvar()
        else:
            raise ValueError(f"Categoria com ID {obj.id} não encontrada.")

    @classmethod
    def excluir(cls, obj):
        """
        Exclui uma categoria existente com base no ID.
        """
        cls.abrir()
        existente = cls.listar_id(obj.id)
        if existente:
            cls.objetos.remove(existente)
            cls.salvar()
        else:
            raise ValueError(f"Categoria com ID {obj.id} não encontrada.")

    @classmethod
    def salvar(cls):
        """
        Salva a lista de categorias no arquivo JSON.
        """
        with open("categorias.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default=vars)

    @classmethod
    def abrir(cls):
        """
        Carrega a lista de categorias do arquivo JSON.
        """
        cls.objetos = []
        try:
            with open("categorias.json", mode="r") as arquivo:
                objetos_json = json.load(arquivo)
                for obj in objetos_json:
                    c = Categoria(obj["id"], obj["descricao"])
                    cls.objetos.append(c)
        except FileNotFoundError:
            pass
