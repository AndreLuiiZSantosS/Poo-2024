class EntradaDeCinema:
  def __init__(self, dia_semana, horario):
    self.dia_semana = dia_semana.lower()
    self.horario = horario

  def calcular_valor(self):
    if self.dia_semana in ["segunda", "terca", "quinta"]:
      valor_base = 16.00
    elif self.dia_semana == "quarta":
      valor_base = 8.00
    elif self.dia_semana == in ["sexta", "sabado", "domingo"]:
      valor_base = 20.00
    else:
      return "Dia da semana inválido."

    if self.horario >= "17":
      valor_base *= 1.5

    if self.dia_semana == "quarta"
      return valor_base, valor_base
else: meia_entrada = valor_base / 2
      return valor_base, meia_entrada

if __name__ == "__main__":
  dia_semana = input("Digite o dia da semana: ")
  horario = float("Digite o horário da sessão (HH:MM): ")

  entrada = EntradaDeCinema(dia_semana, horario)
  valor_inteira, valor_meia = entrada.calcular_valor()

  print(f"Valor da entrada: R${valor_base:.2f}")
      
    