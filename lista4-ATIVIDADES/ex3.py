class Cliente:
    def __init__(self, nome, cpf, limite_credito):
        self._nome = nome
        self._cpf = cpf
        self._limite_credito = limite_credito
        self._socio = None

    def get_nome(self):
        return self._nome

    def get_cpf(self):
        return self._cpf

    def get_limite(self):
        # Retorna o limite considerando o sócio
        if self._socio:
            return self._limite_credito + self._socio._limite_credito
        return self._limite_credito

    def set_nome(self, nome):
        self._nome = nome

    def set_cpf(self, cpf):
        self._cpf = cpf

    def set_limite_credito(self, limite_credito):
        self._limite_credito = limite_credito

    def set_socio(self, socio):
        # Define a sociedade entre dois clientes de forma recíproca
        if isinstance(socio, Cliente) and socio != self:
            self._socio = socio
            socio._socio = self
        else:
            raise ValueError("O sócio deve ser um objeto da classe Cliente e não pode ser o próprio cliente")

    def to_string(self):
        socio_info = f", Sócio: {self._socio.get_nome()}" if self._socio else ""
        return (f"Cliente: {self._nome}, CPF: {self._cpf}, "
                f"Limite de Crédito: R${self.get_limite():.2f}{socio_info}")


class Empresa:
    def __init__(self, nome):
        self._nome = nome
        self._clientes = []

    def get_nome(self):
        return self._nome

    def set_nome(self, nome):
        self._nome = nome

    def inserir(self, cliente):
        if isinstance(cliente, Cliente):
            self._clientes.append(cliente)
        else:
            raise TypeError("O objeto inserido deve ser uma instância da classe Cliente")

    def listar(self):
        return [cliente.to_string() for cliente in self._clientes]

    def to_string(self):
        return f"Empresa: {self._nome}, Número de clientes: {len(self._clientes)}"


# Testando as classes Empresa e Cliente
cliente1 = Cliente("João Silva", "123.456.789-00", 5000)
cliente2 = Cliente("Maria Oliveira", "987.654.321-00", 3000)
cliente3 = Cliente("Carlos Souza", "111.222.333-44", 4000)

# Definindo a sociedade entre clientes
cliente1.set_socio(cliente2)

empresa = Empresa("Cartões XYZ")
empresa.inserir(cliente1)
empresa.inserir(cliente2)
empresa.inserir(cliente3)

print(empresa.to_string())
print("Clientes cadastrados:")
for cliente_info in empresa.listar():
    print(cliente_info)
