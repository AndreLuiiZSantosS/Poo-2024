class viagem:
  
  def __init__(self, distancia_km, horas, minutos):
    self.distancia_km = distancia_km
    self.horas = horas
    self.minutos = minutos

  def calcular_velocidade_media(self):
    tempo_total_horas = self.horas + (self.minutos / 60)
    if tempo_total_horas == 0:
      return 0

    return self.distancia_km / tempo_total_horas

if __name__ == "__main__":
  distancia_km = float(input("Digite a distância percorrida em quilômetros: "))
  horas = int(input("Digite a quantidade de horas: "))
  minutos = int(input("Digite a quantidade de minutos: "))

  viagem = viagem(distancia_km, horas, minutos)
  velocidade_media = viagem.calcular_velocidade_media()

  print(f"Velocidade média: {velocidade_media:.2f} km/h")
  

    
      