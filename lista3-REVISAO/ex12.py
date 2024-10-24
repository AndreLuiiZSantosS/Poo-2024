def main():
  n_teste = 1

  while True:
      # Lê o número de regiões
      N = int(input().strip())

      if N == 0:
          break

      # Inicializa os limites da interseção
      interseccao_esquerda = -10001
      interseccao_superior = 10001
      interseccao_direita = 10001
      interseccao_inferior = -10001

      for _ in range(N):
          X, Y, U, V = map(int, input().strip().split())

          # Atualiza os limites da interseção
          interseccao_esquerda = max(interseccao_esquerda, X)
          interseccao_superior = min(interseccao_superior, Y)
          interseccao_direita = min(interseccao_direita, U)
          interseccao_inferior = max(interseccao_inferior, V)

      # Verifica se há interseção
      print(f"Teste {n_teste}")

      if interseccao_esquerda < interseccao_direita and interseccao_superior > interseccao_inferior:
          print(f"{interseccao_esquerda} {interseccao_superior} {interseccao_direita} {interseccao_inferior}")
      else:
          print("nenhum")

      print()  # Linha em branco entre os casos de teste
      n_teste += 1

if __name__ == "__main__":
  main()
