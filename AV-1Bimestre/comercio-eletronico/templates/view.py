# views.py

class View:
    @staticmethod
    def cliente_autenticar(email, senha):
        """
        Método para autenticar o cliente.
        """
        clientes = [
            {"id": 1, "nome": "André Luiz", "email": "andreluiz@email.com", "senha": "senha123"},
            {"id": 2, "nome": "Maria da Conceição", "email": "maria@email.com", "senha": "senha456"}
        ]
        for cliente in clientes:
            if cliente["email"] == email and cliente["senha"] == senha:
                return cliente
        return None

    @staticmethod
    def cliente_inserir(nome, email, fone, senha):
        novo_cliente = {"id": len(clientes) + 1, "nome": nome, "email": email, "fone": fone, "senha": senha}
        clientes.append(novo_cliente)
        print(f"Cliente {nome} inserido com sucesso!")
        return novo_cliente

    @staticmethod
    def listar_clientes():
        """
        Método para listar todos os clientes.
        """
        return clientes
