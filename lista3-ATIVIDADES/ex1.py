import math

class Retangulo:
    def __init__(self, base, altura):
        # Verifica se os valores são positivos
        if base > 0 and altura > 0:
            self._base = base
            self._altura = altura
        else:
            raise ValueError("Base e altura devem ser valores positivos")

    def set_base(self, base):
        if base > 0:
            self._base = base
        else:
            raise ValueError("A base deve ser um valor positivo")

    def get_base(self):
        return self._base

    def set_altura(self, altura):
        if altura > 0:
            self._altura = altura
        else:
            raise ValueError("A altura deve ser um valor positivo")

    def get_altura(self):
        return self._altura

    def calc_area(self):
        return self._base * self._altura

    def calc_diagonal(self):
        return math.sqrt(self._base ** 2 + self._altura ** 2)

    def to_string(self):
        return f"Retângulo [Base: {self._base}, Altura: {self._altura}, Área: {self.calc_area()}, Diagonal: {self.calc_diagonal():.2f}]"

# Testando a classe Retangulo
try:
    retangulo = Retangulo(5, 3)
    print(retangulo.to_string())

    retangulo.set_base(8)
    retangulo.set_altura(6)
    print("Base:", retangulo.get_base())
    print("Altura:", retangulo.get_altura())
    print("Área:", retangulo.calc_area())
    print("Diagonal:", retangulo.calc_diagonal())
    print(retangulo.to_string())

except ValueError as e:
    print(e)
