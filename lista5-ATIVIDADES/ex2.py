from datetime import datetime
from enum import Enum

class Pagamento(Enum):
    EM_ABERTO = "Em Aberto"
    PAGO_PARCIAL = "Pago Parcial"
    PAGO = "Pago"

class Boleto:
    def __init__(self, codigo_barras, data_emissao, data_vencimento, valor, valor_pago=0):
        """
        Construtor da classe Boleto.
        :param codigo_barras: Código de barras do boleto.
        :param data_emissao: Data de emissão do boleto no formato 'dd/mm/yyyy'.
        :param data_vencimento: Data de vencimento do boleto no formato 'dd/mm/yyyy'.
        :param valor: Valor do boleto.
        :param valor_pago: Valor já pago, que inicia em 0.
        """
        self.codigo_barras = codigo_barras
        self.data_emissao = datetime.strptime(data_emissao, '%d/%m/%Y')
        self.data_vencimento = datetime.strptime(data_vencimento, '%d/%m/%Y')
        self.valor = valor
        self.valor_pago = valor_pago

    def pagar(self, valor_pago):
        """
        Método que registra o pagamento de um boleto.
        :param valor_pago: Valor pago para o boleto.
        :return: None
        """
        if valor_pago <= self.valor - self.valor_pago:
            self.valor_pago += valor_pago
        else:
            raise ValueError("Valor pago não pode ser maior que o valor restante do boleto.")

    def situacao(self):
        """
        Método que retorna a situação do boleto com base no valor pago.
        :return: Situação do boleto.
        """
        if self.valor_pago == 0:
            return Pagamento.EM_ABERTO
        elif self.valor_pago < self.valor:
            return Pagamento.PAGO_PARCIAL
        else:
            return Pagamento.PAGO

    def to_string(self):
        """
        Método que retorna os dados do boleto em formato de string.
        :return: String com os dados do boleto.
        """
        situacao = self.situacao().value
        return f'Código de Barras: {self.codigo_barras}, Emissão: {self.data_emissao.strftime("%d/%m/%Y")}, Vencimento: {self.data_vencimento.strftime("%d/%m/%Y")}, Valor: R${self.valor:.2f}, Pago: R${self.valor_pago:.2f}, Situação: {situacao}'

# Exemplo de uso
if __name__ == "__main__":
    # Criando um boleto
    boleto = Boleto("123456789012345678901234567890123456", "01/11/2024", "15/11/2024", 200.00)

    # Mostrando os dados do boleto antes do pagamento
    print("Dados do Boleto (antes do pagamento):")
    print(boleto.to_string())
    print("\n")

    # Registrando um pagamento parcial
    boleto.pagar(50.00)

    # Mostrando os dados do boleto após o pagamento parcial
    print("Dados do Boleto (após pagamento parcial):")
    print(boleto.to_string())
    print("\n")

    # Registrando o pagamento total
    boleto.pagar(150.00)

    # Mostrando os dados do boleto após pagamento completo
    print("Dados do Boleto (após pagamento total):")
    print(boleto.to_string())
