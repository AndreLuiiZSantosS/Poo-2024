N = int(input())


anterior, atual = 0, 1

# Loop para gerar a sequência de Fibonacci
for i in range(1, N + 1):
    if i == N:
        print(anterior)
    else:
        print(anterior, end=" ")

    # Calcula o próximo valor
    proximo = anterior + atual
    anterior = atual
    atual = proximo