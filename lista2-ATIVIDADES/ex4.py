class EntradaCinema:
  def __init__(self, dia, horario):
    self._dia = dia
    self._horario = horario

  def calcular_valor_ingresso(self):
    valor base = 16.0
      if self._dia in ["sexta", "sabado", "domingo"]:
              valor_base = 20.0
              elif self._dia == "quarta":
                  valor_base = 8.0

      if 17 <= self._horario < 24:
        valor_base *= 1.5

      return valor_base

ingresso = EntradaCinema("quarta",18)
print("valor do ingresso:", ingresso.calcular_valor_ingresso())
