import json

class Persistencia:
    def __init__(self, arquivo):
        """
        Classe base de persistência que fornece métodos genéricos para manipulação de dados.
        :param arquivo: O nome do arquivo onde os dados serão armazenados.
        """
        self.arquivo = arquivo
        self.lista = []

    def inserir(self, obj):
        """
        Insere um objeto na lista.
        :param obj: O objeto a ser inserido.
        """
        self.lista.append(obj)

    def listar(self):
        """
        Retorna todos os objetos da lista.
        :return: Lista de objetos.
        """
        return self.lista

    def listar_id(self, id_obj):
        """
        Retorna um objeto da lista com o id fornecido.
        :param id_obj: ID do objeto a ser buscado.
        :return: Objeto correspondente ao id ou None se não encontrado.
        """
        for obj in self.lista:
            if obj.get_id() == id_obj:
                return obj
        return None

    def atualizar(self, id_obj, novos_dados):
        """
        Atualiza os dados de um objeto na lista.
        :param id_obj: ID do objeto a ser atualizado.
        :param novos_dados: Novo objeto com os dados atualizados.
        """
        obj = self.listar_id(id_obj)
        if obj:
            obj.atualizar_dados(novos_dados)

    def excluir(self, id_obj):
        """
        Exclui um objeto da lista pelo ID.
        :param id_obj: ID do objeto a ser excluído.
        """
        obj = self.listar_id(id_obj)
        if obj:
            self.lista.remove(obj)

    def abrir(self):
        """
        Recupera a lista de objetos de um arquivo JSON.
        """
        try:
            with open(self.arquivo, 'r') as file:
                dados = json.load(file)
                self.lista = [self.criar_objeto(obj) for obj in dados]
        except FileNotFoundError:
            print("Arquivo não encontrado, criando novo arquivo.")
            self.lista = []

    def salvar(self):
        """
        Salva a lista de objetos em um arquivo JSON.
        """
        with open(self.arquivo, 'w') as file:
            dados = [obj.to_dict() for obj in self.lista]
            json.dump(dados, file, indent=4)

    def criar_objeto(self, dados):
        """
        Método que cria um objeto a partir de um dicionário.
        :param dados: Dicionário com os dados do objeto.
        :return: O objeto correspondente.
        """
        raise NotImplementedError("Método 'criar_objeto' deve ser implementado nas subclasses")

class PersistenciaCliente(Persistencia):
    def __init__(self, arquivo="clientes.json"):
        super().__init__(arquivo)

    def criar_objeto(self, dados):
        """
        Cria um objeto Cliente a partir dos dados carregados do JSON.
        :param dados: Dicionário com os dados do cliente.
        :return: Um objeto Cliente.
        """
        return Cliente(dados['id_cliente'], dados['nome'], dados['email'], dados['telefone'])

class PersistenciaVenda(Persistencia):
    def __init__(self, arquivo="vendas.json"):
        super().__init__(arquivo)

    def criar_objeto(self, dados):
        """
        Cria um objeto Venda a partir dos dados carregados do JSON.
        :param dados: Dicionário com os dados da venda.
        :return: Um objeto Venda.
        """
        cliente = PersistenciaCliente().listar_id(dados['id_cliente'])
        venda = Venda(dados['id_venda'], cliente)
        for item in dados['itens']:
            produto = PersistenciaProduto().listar_id(item['id_produto'])
            venda_item = VendaItem(produto, item['quantidade'])
            venda.adicionar_item(venda_item)
        return venda

class PersistenciaVendaItem(Persistencia):
    def __init__(self, arquivo="venda_itens.json"):
        super().__init__(arquivo)

    def criar_objeto(self, dados):
        """
        Cria um objeto VendaItem a partir dos dados carregados do JSON.
        :param dados: Dicionário com os dados do item da venda.
        :return: Um objeto VendaItem.
        """
        produto = PersistenciaProduto().listar_id(dados['id_produto'])
        return VendaItem(produto, dados['quantidade'])

class PersistenciaProduto(Persistencia):
    def __init__(self, arquivo="produtos.json"):
        super().__init__(arquivo)

    def criar_objeto(self, dados):
        """
        Cria um objeto Produto a partir dos dados carregados do JSON.
        :param dados: Dicionário com os dados do produto.
        :return: Um objeto Produto.
        """
        categoria = PersistenciaCategoria().listar_id(dados['id_categoria'])
        return Produto(dados['id_produto'], dados['nome'], dados['preco'], categoria)

class PersistenciaCategoria(Persistencia):
    def __init__(self, arquivo="categorias.json"):
        super().__init__(arquivo)

    def criar_objeto(self, dados):
        """
        Cria um objeto Categoria a partir dos dados carregados do JSON.
        :param dados: Dicionário com os dados da categoria.
        :return: Um objeto Categoria.
        """
        return Categoria(dados['id_categoria'], dados['nome'])


# Exemplo de uso:
if __name__ == "__main__":
    # Persistência de categorias
    persistencia_categoria = PersistenciaCategoria()
    persistencia_categoria.abrir()

    # Persistência de produtos
    persistencia_produto = PersistenciaProduto()
    persistencia_produto.abrir()

    # Persistência de clientes
    persistencia_cliente = PersistenciaCliente()
    persistencia_cliente.abrir()

    # Persistência de vendas
    persistencia_venda = PersistenciaVenda()
    persistencia_venda.abrir()

    # Inserir um novo cliente
    novo_cliente = Cliente(1, "Maria Silva", "maria@example.com", "(11) 91234-5678")
    persistencia_cliente.inserir(novo_cliente)

    # Salvar os dados
    persistencia_cliente.salvar()

    # Listar clientes
    for cliente in persistencia_cliente.listar():
        print(cliente)
