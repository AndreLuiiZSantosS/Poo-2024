import math

class circulo:
  def __init__(self, raio == 0.0):
    self.raio = raio

  def definir_raio(self, raio):
    self._raio = raio

  def obter_raio(self):
    return self._raio

  def calcular_area(self):
    return math.pi * (self._raio ** 2)

  def calcular_circunferencia(self):
    return math.pi * self._raio

calculo = circulo(5)
print("Raio:", circulo.obter_raio())
print("Area:", circulo.calcular_area())
print("circunferencia:", circulo.calcular_circunferencia())
