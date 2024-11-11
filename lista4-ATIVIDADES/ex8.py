n, k = map(int, input().split())
pontos = list(map(int, input().split()))

pontuacoes = [0] * n

for i in range(k):
    pontuacoes[pontos[i] - 1] += 1

print(pontuacoes.index(max(pontuacoes)) + 1)
