class Conversor:
    def __init__(self, num):
        # Verifica se o número é inteiro e positivo
        if isinstance(num, int) and num > 0:
            self._num = num
        else:
            raise ValueError("O número deve ser um inteiro positivo")

    def set_num(self, num):
        if isinstance(num, int) and num > 0:
            self._num = num
        else:
            raise ValueError("O número deve ser um inteiro positivo")

    def get_num(self):
        return self._num

    def binario(self):
        # Retorna a representação binária do número (sem o prefixo '0b')
        return bin(self._num)[2:]

    def to_string(self):
        return f"Número Decimal: {self._num}, Número Binário: {self.binario()}"

# Testando a classe Conversor
try:
    conversor = Conversor(10)
    print(conversor.to_string())

    conversor.set_num(25)
    print("Número Decimal:", conversor.get_num())
    print("Número Binário:", conversor.binario())
    print(conversor.to_string())

except ValueError as e:
    print(e)
