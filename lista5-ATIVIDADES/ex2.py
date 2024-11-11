from enum import Enum

class Pagamento(Enum):
    EM_ABERTO = "Em Aberto"
    PAGO_PARCIAL = "Pago Parcial"
    PAGO = "Pago"

class Boleto:
    def __init__(self, codigo_barras, data_emissao, data_vencimento, valor, valor_pago=0):
        # Atributos do boleto
        self.codigo_barras = codigo_barras
        self.data_emissao = datetime.strptime(data_emissao, '%d/%m/%Y')
        self.data_vencimento = datetime.strptime(data_vencimento, '%d/%m/%Y')
        self.valor = valor
        self.valor_pago = valor_pago

    def pagar(self, valor_pago):
        # Atualiza o valor pago
        if valor_pago <= self.valor - self.valor_pago:
            self.valor_pago += valor_pago
        else:
            raise ValueError("Valor pago não pode ser maior que o valor do boleto.")

    def situacao(self):
        # Verificando a situação de pagamento
        if self.valor_pago == 0:
            return Pagamento.EM_ABERTO
        elif self.valor_pago < self.valor:
            return Pagamento.PAGO_PARCIAL
        else:
            return Pagamento.PAGO

    def to_string(self):
        # Retornando uma string com os atributos do boleto
        return f"Código de Barras: {self.codigo_barras}\nData de Emissão: {self.data_emissao.strftime('%d/%m/%Y')}\nData de Vencimento: {self.data_vencimento.strftime('%d/%m/%Y')}\nValor: R$ {self.valor:.2f}\nValor Pago: R$ {self.valor_pago:.2f}\nSituação: {self.situacao().value}"
