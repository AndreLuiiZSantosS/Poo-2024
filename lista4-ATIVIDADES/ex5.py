n = int(input())
valores = list(map(int, input().split()))

menor_valor = min(valores)
posicao = valores.index(menor_valor)

print(f"Menor valor: {menor_valor}")
print(f"Posicao: {posicao}")
