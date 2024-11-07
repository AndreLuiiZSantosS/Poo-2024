class viagem:
  def __init__ (self,distancia= 0.0, tempo = 0.0):
    self._distancia = distancia
    self._tempo = tempo

  def definir_distancia(self,distancia):
    self._distancia = distancia

  def obter_distancia(self)
    return self._distancia

  def definir_tempo(self, tempo):
    self._tempo = tempo

  def obter_tempo(self)
    return self._tempo

  def calcular_velociade_media(self):
    if self._tempo > 0:
      return self._distancia / self._tempo
    else:
      return 0:

viagem = viagem (100, 2)

print("Distancia:", viagem.obter_distancia())

print("Tempo:", viagem.obter_tempo())

print("Distancia:", viagem.calcular_velocidade_media())
