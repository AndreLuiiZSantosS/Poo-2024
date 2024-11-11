class Cliente:
    def __init__(self, id_cliente, nome, email, telefone):
        """
        Construtor da classe Cliente.
        :param id_cliente: Identificador único do cliente.
        :param nome: Nome do cliente.
        :param email: Email do cliente.
        :param telefone: Telefone do cliente.
        """
        self.id_cliente = id_cliente
        self.nome = nome
        self.email = email
        self.telefone = telefone

    def __str__(self):
        """
        Método que retorna as informações do cliente em formato de string.
        :return: String com as informações do cliente.
        """
        return f"ID: {self.id_cliente}, Nome: {self.nome}, Email: {self.email}, Telefone: {self.telefone}"

    # Métodos Get e Set
    def get_id_cliente(self):
        return self.id_cliente

    def set_nome(self, nome):
        self.nome = nome

    def get_nome(self):
        return self.nome

    def set_email(self, email):
        self.email = email

    def get_email(self):
        return self.email

    def set_telefone(self, telefone):
        self.telefone = telefone

    def get_telefone(self):
        return self.telefone


class Categoria:
    def __init__(self, id_categoria, nome):
        """
        Construtor da classe Categoria.
        :param id_categoria: Identificador único da categoria.
        :param nome: Nome da categoria.
        """
        self.id_categoria = id_categoria
        self.nome = nome

    def __str__(self):
        """
        Método que retorna as informações da categoria em formato de string.
        :return: String com as informações da categoria.
        """
        return f"ID: {self.id_categoria}, Nome: {self.nome}"

    # Métodos Get e Set
    def get_id_categoria(self):
        return self.id_categoria

    def set_nome(self, nome):
        self.nome = nome

    def get_nome(self):
        return self.nome


class Produto:
    def __init__(self, id_produto, nome, preco, categoria):
        """
        Construtor da classe Produto.
        :param id_produto: Identificador único do produto.
        :param nome: Nome do produto.
        :param preco: Preço do produto.
        :param categoria: Categoria do produto.
        """
        self.id_produto = id_produto
        self.nome = nome
        self.preco = preco
        self.categoria = categoria  # Instância de Categoria

    def __str__(self):
        """
        Método que retorna as informações do produto em formato de string.
        :return: String com as informações do produto.
        """
        return f"ID: {self.id_produto}, Nome: {self.nome}, Preço: {self.preco}, Categoria: {self.categoria.get_nome()}"

    # Métodos Get e Set
    def get_id_produto(self):
        return self.id_produto

    def set_nome(self, nome):
        self.nome = nome

    def get_nome(self):
        return self.nome

    def set_preco(self, preco):
        self.preco = preco

    def get_preco(self):
        return self.preco

    def set_categoria(self, categoria):
        self.categoria = categoria

    def get_categoria(self):
        return self.categoria


class VendaItem:
    def __init__(self, produto, quantidade):
        """
        Construtor da classe VendaItem.
        :param produto: Instância de Produto.
        :param quantidade: Quantidade do produto.
        """
        self.produto = produto
        self.quantidade = quantidade

    def __str__(self):
        """
        Método que retorna as informações do item da venda em formato de string.
        :return: String com as informações do item da venda.
        """
        return f"Produto: {self.produto.get_nome()}, Quantidade: {self.quantidade}, Preço Unitário: {self.produto.get_preco()}"

    # Métodos Get e Set
    def get_produto(self):
        return self.produto

    def set_produto(self, produto):
        self.produto = produto

    def get_quantidade(self):
        return self.quantidade

    def set_quantidade(self, quantidade):
        self.quantidade = quantidade


class Venda:
    def __init__(self, id_venda, cliente):
        """
        Construtor da classe Venda.
        :param id_venda: Identificador único da venda.
        :param cliente: Instância de Cliente.
        """
        self.id_venda = id_venda
        self.cliente = cliente  # Instância de Cliente
        self.itens = []  # Lista de VendaItem

    def __str__(self):
        """
        Método que retorna as informações da venda em formato de string.
        :return: String com as informações da venda.
        """
        itens_str = "\n".join(str(item) for item in self.itens)
        return f"Venda ID: {self.id_venda}, Cliente: {self.cliente.get_nome()}\nItens da Venda:\n{itens_str}"

    # Métodos Get e Set
    def get_id_venda(self):
        return self.id_venda

    def set_cliente(self, cliente):
        self.cliente = cliente

    def get_cliente(self):
        return self.cliente

    def adicionar_item(self, venda_item):
        """Adiciona um item à venda."""
        self.itens.append(venda_item)

    def calcular_total(self):
        """Calcula o total da venda."""
        total = sum(item.get_quantidade() * item.get_produto().get_preco() for item in self.itens)
        return total


# Exemplo de uso:
if __name__ == "__main__":
    # Criando categorias
    categoria1 = Categoria(1, "Eletrônicos")
    categoria2 = Categoria(2, "Roupas")

    # Criando produtos
    produto1 = Produto(1, "Smartphone", 1500.00, categoria1)
    produto2 = Produto(2, "Camiseta", 50.00, categoria2)

    # Criando cliente
    cliente = Cliente(1, "João Silva", "joao@example.com", "(11) 98765-4321")

    # Criando venda e adicionando itens
    venda = Venda(1, cliente)
    venda_item1 = VendaItem(produto1, 1)
    venda_item2 = VendaItem(produto2, 3)
    venda.adicionar_item(venda_item1)
    venda.adicionar_item(venda_item2)

    # Exibindo informações
    print(venda)
    print(f"Total da venda: R${venda.calcular_total():.2f}")
