# Classe para representar Produtos
class Produto:
    def __init__(self, id_produto, nome, preco, categoria):
        self.id_produto = id_produto
        self.nome = nome
        self.preco = preco
        self.categoria = categoria

    def __str__(self):
        return f"{self.nome} - R${self.preco:.2f} ({self.categoria})"

# Classe para representar Categorias
class Categoria:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return self.nome

# Classe para representar Pedidos
class Pedido:
    def __init__(self, id_pedido, cliente, produtos):
        self.id_pedido = id_pedido
        self.cliente = cliente
        self.produtos = produtos
        self.total = sum(produto.preco for produto in produtos)

    def __str__(self):
        return f"Pedido #{self.id_pedido} - Cliente: {self.cliente}\nTotal: R${self.total:.2f}\nProdutos:\n" + \
               "\n".join([f"- {produto}" for produto in self.produtos])

# Classe para representar Clientes
class Cliente:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.carrinho = []
        self.pedidos = []

    def adicionar_ao_carrinho(self, produto):
        self.carrinho.append(produto)
        print(f"Produto '{produto.nome}' adicionado ao carrinho.")

    def comprar_carrinho(self):
        if not self.carrinho:
            print("O carrinho está vazio!")
            return
        novo_pedido = Pedido(len(self.pedidos) + 1, self.nome, self.carrinho)
        self.pedidos.append(novo_pedido)
        self.carrinho = []
        print(f"Compra realizada com sucesso! {novo_pedido}")

    def visualizar_pedidos(self):
        if not self.pedidos:
            print("Nenhum pedido encontrado.")
            return
        for pedido in self.pedidos:
            print(pedido)

# Classe para representar Visitantes
class Visitante:
    def abrir_conta(self, nome, email, senha):
        return Cliente(nome, email, senha)

# Classe para representar Admin
class Admin:
    def __init__(self):
        self.clientes = []
        self.produtos = []
        self.categorias = []

    def manter_cadastro_clientes(self, cliente):
        self.clientes.append(cliente)
        print(f"Cliente '{cliente.nome}' cadastrado com sucesso.")

    def manter_cadastro_categorias(self, categoria):
        self.categorias.append(categoria)
        print(f"Categoria '{categoria.nome}' cadastrada com sucesso.")

    def manter_cadastro_produtos(self, produto):
        self.produtos.append(produto)
        print(f"Produto '{produto.nome}' cadastrado com sucesso.")

    def reajustar_precos(self, percentual):
        for produto in self.produtos:
            produto.preco += produto.preco * (percentual / 100)
        print(f"Reajuste de {percentual}% aplicado a todos os produtos.")

    def visualizar_pedidos(self, clientes):
        for cliente in clientes:
            cliente.visualizar_pedidos()
