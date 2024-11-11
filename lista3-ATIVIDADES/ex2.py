class Frete:
    def __init__(self, distancia, peso):
        # Verifica se os valores são positivos
        if distancia > 0 and peso > 0:
            self._distancia = distancia
            self._peso = peso
        else:
            raise ValueError("Distância e peso devem ser valores positivos")

    def set_distancia(self, distancia):
        if distancia > 0:
            self._distancia = distancia
        else:
            raise ValueError("A distância deve ser um valor positivo")

    def get_distancia(self):
        return self._distancia

    def set_peso(self, peso):
        if peso > 0:
            self._peso = peso
        else:
            raise ValueError("O peso deve ser um valor positivo")

    def get_peso(self):
        return self._peso

    def calc_frete(self):
        # Calcula o frete como 0,01 real por kg por km
        return self._distancia * self._peso * 0.01

    def to_string(self):
        return (f"Frete [Distância: {self._distancia} km, "
                f"Peso: {self._peso} kg, "
                f"Valor do Frete: R$ {self.calc_frete():.2f}]")

# Testando a classe Frete
try:
    frete = Frete(200, 50)
    print(frete.to_string())

    frete.set_distancia(300)
    frete.set_peso(75)
    print("Distância:", frete.get_distancia())
    print("Peso:", frete.get_peso())
    print("Valor do Frete:", frete.calc_frete())
    print(frete.to_string())

except ValueError as e:
    print(e)
