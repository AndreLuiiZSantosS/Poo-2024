from datetime import datetime

class Paciente:
    def __init__(self, nome, cpf, telefone, nascimento):
        """
        Construtor da classe Paciente.
        :param nome: Nome do paciente.
        :param cpf: CPF do paciente.
        :param telefone: Telefone do paciente.
        :param nascimento: Data de nascimento do paciente no formato 'dd/mm/yyyy'.
        """
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.nascimento = datetime.strptime(nascimento, '%d/%m/%Y')

    def idade(self):
        """
        Método que calcula a idade do paciente em anos e meses.
        :return: Texto com a idade do paciente em anos e meses.
        """
        hoje = datetime.today()
        anos = hoje.year - self.nascimento.year
        meses = hoje.month - self.nascimento.month
        
        if meses < 0:
            anos -= 1
            meses += 12
        
        return f'{anos} anos e {meses} meses'

    def to_string(self):
        """
        Método que retorna os dados do paciente em formato de string.
        :return: String com os dados do paciente.
        """
        return f'Nome: {self.nome}, CPF: {self.cpf}, Telefone: {self.telefone}, Nascimento: {self.nascimento.strftime("%d/%m/%Y")}'

# Exemplo de uso
if __name__ == "__main__":
    # Criando um paciente
    paciente = Paciente("João da Silva", "123.456.789-00", "(84) 98765-4321", "15/08/1985")

    # Mostrando os dados do paciente e sua idade
    print("Dados do Paciente:")
    print(paciente.to_string())
    print("Idade:", paciente.idade())
