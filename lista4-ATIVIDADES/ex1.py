import random

class Bingo:
    def __init__(self, num_bolas):
        if num_bolas > 0:
            self._num_bolas = num_bolas
            self._bolas_sorteadas = []
            self._todas_bolas = list(range(1, num_bolas + 1))
        else:
            raise ValueError("O número de bolas deve ser maior que zero")

    def proximo(self):
        """Sorteia uma bola e retorna o seu número ou -1 se todas já foram sorteadas."""
        if len(self._bolas_sorteadas) < self._num_bolas:
            bola = random.choice(self._todas_bolas)
            self._todas_bolas.remove(bola)
            self._bolas_sorteadas.append(bola)
            return bola
        else:
            return -1  # Indica que todas as bolas já foram sorteadas

    def sorteados(self):
        """Retorna uma lista com todas as bolas já sorteadas."""
        return self._bolas_sorteadas

    def to_string(self):
        """Retorna uma representação textual do estado atual do jogo."""
        return (f"Número de bolas: {self._num_bolas}\n"
                f"Bolas sorteadas: {', '.join(map(str, self._bolas_sorteadas)) if self._bolas_sorteadas else 'Nenhuma'}")

# Testando a classe Bingo
try:
    bingo = Bingo(10)  # Iniciando o jogo com 10 bolas
    print(bingo.to_string())

    print("Sorteando bolas:")
    for _ in range(12):  # Tentativa de sorteio de mais bolas do que o limite
        bola = bingo.proximo()
        if bola == -1:
            print("Todas as bolas já foram sorteadas.")
        else:
            print(f"Bola sorteada: {bola}")

    print("Bolas sorteadas:", bingo.sorteados())
    print(bingo.to_string())

except ValueError as e:
    print(e)
