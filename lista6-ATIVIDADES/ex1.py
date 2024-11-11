import json

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

    def get_id_cliente(self):
        """Retorna o ID do cliente."""
        return self.id_cliente

    def set_nome(self, nome):
        """Altera o nome do cliente."""
        self.nome = nome

    def get_nome(self):
        """Retorna o nome do cliente."""
        return self.nome

    def set_email(self, email):
        """Altera o email do cliente."""
        self.email = email

    def get_email(self):
        """Retorna o email do cliente."""
        return self.email

    def set_telefone(self, telefone):
        """Altera o telefone do cliente."""
        self.telefone = telefone

    def get_telefone(self):
        """Retorna o telefone do cliente."""
        return self.telefone


class Clientes:
    lista_clientes = []

    @classmethod
    def inserir(cls, cliente):
        """Insere um cliente na lista de clientes."""
        cls.lista_clientes.append(cliente)

    @classmethod
    def listar(cls):
        """Lista todos os clientes."""
        return cls.lista_clientes

    @classmethod
    def listar_id(cls, id_cliente):
        """Retorna o cliente com o id fornecido."""
        for cliente in cls.lista_clientes:
            if cliente.get_id_cliente() == id_cliente:
                return cliente
        return None

    @classmethod
    def atualizar(cls, id_cliente, nome=None, email=None, telefone=None):
        """Atualiza os dados do cliente com o id fornecido."""
        cliente = cls.listar_id(id_cliente)
        if cliente:
            if nome:
                cliente.set_nome(nome)
            if email:
                cliente.set_email(email)
            if telefone:
                cliente.set_telefone(telefone)
            return True
        return False

    @classmethod
    def excluir(cls, id_cliente):
        """Exclui o cliente com o id fornecido."""
        cliente = cls.listar_id(id_cliente)
        if cliente:
            cls.lista_clientes.remove(cliente)
            return True
        return False

    @classmethod
    def abrir(cls, arquivo):
        """Abre e carrega os clientes a partir de um arquivo JSON."""
        try:
            with open(arquivo, 'r') as f:
                dados = json.load(f)
                cls.lista_clientes = [Cliente(**cliente) for cliente in dados]
        except FileNotFoundError:
            print(f"O arquivo {arquivo} não foi encontrado.")
        except json.JSONDecodeError:
            print(f"O arquivo {arquivo} não pôde ser decodificado.")

    @classmethod
    def salvar(cls, arquivo):
        """Salva a lista de clientes em um arquivo JSON."""
        with open(arquivo, 'w') as f:
            json.dump([cliente.__dict__ for cliente in cls.lista_clientes], f, indent=4)

# Exemplo de uso
if __name__ == "__main__":
    # Inserindo clientes
    cliente1 = Cliente(1, "João Silva", "joao@example.com", "(11) 98765-4321")
    cliente2 = Cliente(2, "Maria Oliveira", "maria@example.com", "(11) 91234-5678")
    
    Clientes.inserir(cliente1)
    Clientes.inserir(cliente2)

    # Listando todos os clientes
    print("Clientes cadastrados:")
    for cliente in Clientes.listar():
        print(cliente)

    # Atualizando um cliente
    Clientes.atualizar(1, nome="João Carlos Silva", telefone="(11) 99876-5432")

    # Excluindo um cliente
    Clientes.excluir(2)

    # Salvando os dados em um arquivo JSON
    Clientes.salvar("clientes.json")

    # Abrindo os dados a partir de um arquivo JSON
    Clientes.abrir("clientes.json")

    # Listando os clientes após carregar do arquivo
    print("\nClientes após carregar do arquivo JSON:")
    for cliente in Clientes.listar():
        print(cliente)
