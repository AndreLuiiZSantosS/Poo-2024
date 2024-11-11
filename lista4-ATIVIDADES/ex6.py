matriz = []
for i in range(12):
    linha = []
    for j in range(12):
        linha.append(float(input()))
    matriz.append(linha)

soma = 0
contagem = 0

for i in range(12):
    for j in range(i + 1, 12):  # Considera apenas elementos acima da diagonal principal
        soma += matriz[i][j]
        contagem += 1

print(f"Soma: {soma:.1f}")
# Se desejar calcular a média, use: print(f"Média: {soma / contagem:.1f}")
