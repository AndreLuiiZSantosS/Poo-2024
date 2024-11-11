import datetime

class Data:
    def __init__(self, dia, mes, ano):
        # Verifica se a data é válida
        if self._data_valida(dia, mes, ano):
            self._dia = dia
            self._mes = mes
            self._ano = ano
        else:
            raise ValueError("Data inválida")

    def _data_valida(self, dia, mes, ano):
        """Verifica se a data é válida."""
        try:
            datetime.date(ano, mes, dia)
            return True
        except ValueError:
            return False

    def get_dia(self):
        return self._dia

    def get_mes(self):
        return self._mes

    def get_ano(self):
        return self._ano

    def set_data(self, data_str):
        """Recebe uma string no formato 'dd/mm/aaaa' e armazena a data, validando-a."""
        try:
            dia, mes, ano = map(int, data_str.split('/'))
            if self._data_valida(dia, mes, ano):
                self._dia = dia
                self._mes = mes
                self._ano = ano
            else:
                raise ValueError("Data inválida")
        except (ValueError, IndexError):
            raise ValueError("Formato de data inválido")

    def to_string(self):
        """Retorna a data no formato 'dd/mm/aaaa'."""
        return f"{self._dia:02d}/{self._mes:02d}/{self._ano:04d}"

# Testando a classe Data
try:
    data = Data(25, 12, 2023)
    print(data.to_string())

    data.set_data("01/01/2024")
    print("Dia:", data.get_dia())
    print("Mês:", data.get_mes())
    print("Ano:", data.get_ano())
    print(data.to_string())

except ValueError as e:
    print(e)
