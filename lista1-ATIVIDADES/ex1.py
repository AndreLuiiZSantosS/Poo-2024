import math

class circulo:
  def __init__(self, raio):
    self.raio = raio

  def caucluar-area(self):
    return math.pi * (self.raio ** 2)

  def calcular-circunferencia(self):
    return 2 * math.pi * self.raio

if __name__ == "__main__":
    raio = float(input("Digite o raio do círculo: "))
    circulo = circulo(raio)

    area = circulo.calcular_area()
    circunferencia = circulo.calcular_circunferencia()
    print(f"Área do círculo: {area:.2f}")
    print(f"Circunferência do círculo: {circunferencia:.2f}" )
  



      