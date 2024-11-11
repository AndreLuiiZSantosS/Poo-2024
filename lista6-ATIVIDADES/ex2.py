class UI:
    def __init__(self):
        self.clientes = Clientes()  # Instância da classe Clientes

    def menu(self):
        """
        Exibe o menu de opções para o usuário.
        """
        print("\nMenu de Operações:")
        print("1 - Listar clientes")
        print("2 - Inserir cliente")
        print("3 - Atualizar cliente")
        print("4 - Excluir cliente")
        print("5 - Finalizar aplicação")

    def listar_clientes(self):
        """
        Exibe os clientes cadastrados.
        """
        print("\nClientes cadastrados:")
        clientes = self.clientes.listar()
        if clientes:
            for cliente in clientes:
                print(cliente)
        else:
            print("Nenhum cliente cadastrado.")

    def ler_dados_cliente(self):
        """
        Lê os dados do cliente fornecidos pelo usuário.
        :return: Retorna um dicionário com os dados do cliente.
        """
        id_cliente = int(input("Digite o ID do cliente: "))
        nome = input("Digite o nome do cliente: ")
        email = input("Digite o email do cliente: ")
        telefone = input("Digite o telefone do cliente: ")
        return id_cliente, nome, email, telefone

    def inserir_cliente(self):
        """
        Lê os dados de um cliente e o insere na lista de clientes.
        """
        print("\nInserir novo cliente:")
        id_cliente, nome, email, telefone = self.ler_dados_cliente()
        cliente = Cliente(id_cliente, nome, email, telefone)
        self.clientes.inserir(cliente)
        print(f"Cliente {nome} inserido com sucesso!")

    def atualizar_cliente(self):
        """
        Atualiza os dados de um cliente existente.
        """
        print("\nAtualizar dados de um cliente:")
        id_cliente = int(input("Digite o ID do cliente a ser atualizado: "))
        cliente = self.clientes.listar_id(id_cliente)
        if cliente:
            nome = input(f"Digite o novo nome (atual: {cliente.get_nome()}): ") or cliente.get_nome()
            email = input(f"Digite o novo email (atual: {cliente.get_email()}): ") or cliente.get_email()
            telefone = input(f"Digite o novo telefone (atual: {cliente.get_telefone()}): ") or cliente.get_telefone()
            self.clientes.atualizar(id_cliente, nome, email, telefone)
            print(f"Cliente ID {id_cliente} atualizado com sucesso!")
        else:
            print(f"Cliente com ID {id_cliente} não encontrado.")

    def excluir_cliente(self):
        """
        Exclui um cliente da lista de clientes.
        """
        print("\nExcluir cliente:")
        id_cliente = int(input("Digite o ID do cliente a ser excluído: "))
        if self.clientes.excluir(id_cliente):
            print(f"Cliente ID {id_cliente} excluído com sucesso!")
        else:
            print(f"Cliente com ID {id_cliente} não encontrado.")

    def main(self):
        """
        Método principal que mantém o laço de interação até o usuário decidir finalizar.
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
                print("Finalizando a aplicação...")
                break
            else:
                print("Opção inválida. Tente novamente.")

# Exemplo de uso
if __name__ == "__main__":
    ui = UI()
    ui.main()
