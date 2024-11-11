from datetime import datetime

class Paciente:
    def __init__(self, nome, cpf, telefone, nascimento):
        # Atributos do paciente
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.nascimento = datetime.strptime(nascimento, '%d/%m/%Y')  # Data de nascimento em formato dd/mm/aaaa

    def idade(self):
        # Calculando a idade em anos e meses
        hoje = datetime.today()
        anos = hoje.year - self.nascimento.year
        meses = hoje.month - self.nascimento.month
        if meses < 0:
            anos -= 1
            meses += 12
        return f"{anos} anos e {meses} meses"

    def to_string(self):
        # Retornando uma string com os atributos do paciente
        return f"Nome: {self.nome}\nCPF: {self.cpf}\nTelefone: {self.telefone}\nNascimento: {self.nascimento.strftime('%d/%m/%Y')}\nIdade: {self.idade()}"
