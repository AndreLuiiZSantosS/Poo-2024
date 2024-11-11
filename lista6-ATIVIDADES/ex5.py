class UI:
    def __init__(self):
        """
        Inicializa a interface de usuário com as instâncias de persistência para Cliente, Produto e Categoria.
        """
        self.persistencia_cliente = PersistenciaCliente()
        self.persistencia_produto = PersistenciaProduto()
        self.persistencia_categoria = PersistenciaCategoria()

        # Carrega os dados iniciais dos arquivos JSON
        self.persistencia_cliente.abrir()
        self.persistencia_produto.abrir()
        self.persistencia_categoria.abrir()

    def menu(self):
        """
        Exibe o menu com as opções de CRUD para clientes, categorias e produtos.
        """
        print("\nMenu de Operações:")
        print("1. Listar Clientes")
        print("2. Inserir Cliente")
        print("3. Atualizar Cliente")
        print("4. Excluir Cliente")
        print("5. Listar Categorias")
        print("6. Inserir Categoria")
        print("7. Atualizar Categoria")
        print("8. Excluir Categoria")
        print("9. Listar Produtos")
        print("10. Inserir Produto")
        print("11. Atualizar Produto")
        print("12. Excluir Produto")
        print("13. Finalizar")
    
    def listar_clientes(self):
        """
        Exibe todos os clientes cadastrados.
        """
        print("\nClientes Cadastrados:")
        clientes = self.persistencia_cliente.listar()
        if not clientes:
            print("Nenhum cliente encontrado.")
        for cliente in clientes:
            print(cliente)

    def inserir_cliente(self):
        """
        Lê os dados de um cliente e insere na lista de clientes.
        """
        print("\nInserir Cliente:")
        id_cliente = int(input("Digite o ID do cliente: "))
        nome = input("Digite o nome do cliente: ")
        email = input("Digite o e-mail do cliente: ")
        telefone = input("Digite o telefone do cliente: ")
        
        cliente = Cliente(id_cliente, nome, email, telefone)
        self.persistencia_cliente.inserir(cliente)
        self.persistencia_cliente.salvar()
        print("Cliente inserido com sucesso!")

    def atualizar_cliente(self):
        """
        Lê os dados de um cliente para atualizar os dados na lista de clientes.
        """
        print("\nAtualizar Cliente:")
        id_cliente = int(input("Digite o ID do cliente a ser atualizado: "))
        cliente = self.persistencia_cliente.listar_id(id_cliente)
        if cliente:
            nome = input(f"Novo nome ({cliente.get_nome()}): ")
            email = input(f"Novo e-mail ({cliente.get_email()}): ")
            telefone = input(f"Novo telefone ({cliente.get_telefone()}): ")

            cliente.set_nome(nome if nome else cliente.get_nome())
            cliente.set_email(email if email else cliente.get_email())
            cliente.set_telefone(telefone if telefone else cliente.get_telefone())

            self.persistencia_cliente.atualizar(id_cliente, cliente)
            self.persistencia_cliente.salvar()
            print("Cliente atualizado com sucesso!")
        else:
            print("Cliente não encontrado.")

    def excluir_cliente(self):
        """
        Exclui um cliente da lista de clientes.
        """
        print("\nExcluir Cliente:")
        id_cliente = int(input("Digite o ID do cliente a ser excluído: "))
        cliente = self.persistencia_cliente.listar_id(id_cliente)
        if cliente:
            self.persistencia_cliente.excluir(id_cliente)
            self.persistencia_cliente.salvar()
            print("Cliente excluído com sucesso!")
        else:
            print("Cliente não encontrado.")

    def listar_categorias(self):
        """
        Exibe todas as categorias cadastradas.
        """
        print("\nCategorias Cadastradas:")
        categorias = self.persistencia_categoria.listar()
        if not categorias:
            print("Nenhuma categoria encontrada.")
        for categoria in categorias:
            print(categoria)

    def inserir_categoria(self):
        """
        Lê os dados de uma categoria e insere na lista de categorias.
        """
        print("\nInserir Categoria:")
        id_categoria = int(input("Digite o ID da categoria: "))
        nome_categoria = input("Digite o nome da categoria: ")

        categoria = Categoria(id_categoria, nome_categoria)
        self.persistencia_categoria.inserir(categoria)
        self.persistencia_categoria.salvar()
        print("Categoria inserida com sucesso!")

    def atualizar_categoria(self):
        """
        Lê os dados de uma categoria para atualizar os dados na lista de categorias.
        """
        print("\nAtualizar Categoria:")
        id_categoria = int(input("Digite o ID da categoria a ser atualizada: "))
        categoria = self.persistencia_categoria.listar_id(id_categoria)
        if categoria:
            nome_categoria = input(f"Novo nome ({categoria.get_nome()}): ")

            categoria.set_nome(nome_categoria if nome_categoria else categoria.get_nome())
            self.persistencia_categoria.atualizar(id_categoria, categoria)
            self.persistencia_categoria.salvar()
            print("Categoria atualizada com sucesso!")
        else:
            print("Categoria não encontrada.")

    def excluir_categoria(self):
        """
        Exclui uma categoria da lista de categorias.
        """
        print("\nExcluir Categoria:")
        id_categoria = int(input("Digite o ID da categoria a ser excluída: "))
        categoria = self.persistencia_categoria.listar_id(id_categoria)
        if categoria:
            self.persistencia_categoria.excluir(id_categoria)
            self.persistencia_categoria.salvar()
            print("Categoria excluída com sucesso!")
        else:
            print("Categoria não encontrada.")

    def listar_produtos(self):
        """
        Exibe todos os produtos cadastrados.
        """
        print("\nProdutos Cadastrados:")
        produtos = self.persistencia_produto.listar()
        if not produtos:
            print("Nenhum produto encontrado.")
        for produto in produtos:
            print(produto)

    def inserir_produto(self):
        """
        Lê os dados de um produto e insere na lista de produtos.
        """
        print("\nInserir Produto:")
        id_produto = int(input("Digite o ID do produto: "))
        nome_produto = input("Digite o nome do produto: ")
        preco_produto = float(input("Digite o preço do produto: "))
        id_categoria = int(input("Digite o ID da categoria: "))
        categoria = self.persistencia_categoria.listar_id(id_categoria)
        
        if categoria:
            produto = Produto(id_produto, nome_produto, preco_produto, categoria)
            self.persistencia_produto.inserir(produto)
            self.persistencia_produto.salvar()
            print("Produto inserido com sucesso!")
        else:
            print("Categoria não encontrada.")

    def atualizar_produto(self):
        """
        Lê os dados de um produto para atualizar os dados na lista de produtos.
        """
        print("\nAtualizar Produto:")
        id_produto = int(input("Digite o ID do produto a ser atualizado: "))
        produto = self.persistencia_produto.listar_id(id_produto)
        if produto:
            nome_produto = input(f"Novo nome ({produto.get_nome()}): ")
            preco_produto = input(f"Novo preço ({produto.get_preco()}): ")

            produto.set_nome(nome_produto if nome_produto else produto.get_nome())
            produto.set_preco(float(preco_produto) if preco_produto else produto.get_preco())

            self.persistencia_produto.atualizar(id_produto, produto)
            self.persistencia_produto.salvar()
            print("Produto atualizado com sucesso!")
        else:
            print("Produto não encontrado.")

    def excluir_produto(self):
        """
        Exclui um produto da lista de produtos.
        """
        print("\nExcluir Produto:")
        id_produto = int(input("Digite o ID do produto a ser excluído: "))
        produto = self.persistencia_produto.listar_id(id_produto)
        if produto:
            self.persistencia_produto.excluir(id_produto)
            self.persistencia_produto.salvar()
            print("Produto excluído com sucesso!")
        else:
            print("Produto não encontrado.")

    def main(self):
        """
        Método principal que mantém o laço de interação com o usuário até que uma opção de finalização seja escolhida.
        """
        while True:
            self.menu()
            opcao = input("Escolha uma opção: ")
            
            if opcao == '1':
                self.listar_clientes()
            elif opcao == '2':
                self.inserir_cliente()
            elif opcao == '3':
                self.atualizar_cliente()
            elif opcao == '4':
                self.excluir_cliente()
            elif opcao == '5':
                self.listar_categorias()
            elif opcao == '6':
                self.inserir_categoria()
            elif opcao == '7':
                self.atualizar_categoria()
            elif opcao == '8':
                self.excluir_categoria()
            elif opcao == '9':
                self.listar_produtos()
            elif opcao == '10':
                self.inserir_produto()
            elif opcao == '11':
                self.atualizar_produto()
            elif opcao == '12':
                self.excluir_produto()
            elif opcao == '13':
                print("Finalizando a aplicação...")
                break
            else:
                print("Opção inválida! Tente novamente.")
