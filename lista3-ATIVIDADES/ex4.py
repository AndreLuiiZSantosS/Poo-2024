import math

class EquacaoSegundoGrau:
    def __init__(self, a, b, c):
        # Verifica se 'a' é diferente de zero, pois uma equação do 2º grau requer isso
        if a != 0:
            self._a = a
            self._b = b
            self._c = c
        else:
            raise ValueError("O coeficiente 'a' deve ser diferente de zero para ser uma equação do 2º grau")

    def set_a(self, a):
        if a != 0:
            self._a = a
        else:
            raise ValueError("O coeficiente 'a' deve ser diferente de zero para ser uma equação do 2º grau")

    def get_a(self):
        return self._a

    def set_b(self, b):
        self._b = b

    def get_b(self):
        return self._b

    def set_c(self, c):
        self._c = c

    def get_c(self):
        return self._c

    def delta(self):
        # Calcula o delta (b^2 - 4ac)
        return (self._b ** 2) - (4 * self._a * self._c)

    def tem_raizes_reais(self):
        # Verifica se o delta é maior ou igual a zero
        return self.delta() >= 0

    def raiz1(self):
        if self.tem_raizes_reais():
            return (-self._b + math.sqrt(self.delta())) / (2 * self._a)
        else:
            return None  # Retorna None se não houver raízes reais

    def raiz2(self):
        if self.tem_raizes_reais():
            return (-self._b - math.sqrt(self.delta())) / (2 * self._a)
        else:
            return None  # Retorna None se não houver raízes reais

    def to_string(self):
        raizes = "não existem raízes reais" if not self.tem_raizes_reais() else f"Raiz 1: {self.raiz1():.2f}, Raiz 2: {self.raiz2():.2f}"
        return (f"Equação: {self._a}x² + {self._b}x + {self._c}\n"
                f"Delta: {self.delta():.2f}\n"
                f"{raizes}")

# Testando a classe EquacaoSegundoGrau
try:
    equacao = EquacaoSegundoGrau(1, -3, 2)
    print(equacao.to_string())

    equacao.set_a(1)
    equacao.set_b(2)
    equacao.set_c(1)
    print("Coeficiente a:", equacao.get_a())
    print("Coeficiente b:", equacao.get_b())
    print("Coeficiente c:", equacao.get_c())
    print("Delta:", equacao.delta())
    print("Tem raízes reais:", equacao.tem_raizes_reais())
    print("Raiz 1:", equacao.raiz1())
    print("Raiz 2:", equacao.raiz2())
    print(equacao.to_string())

except ValueError as e:
    print(e)
