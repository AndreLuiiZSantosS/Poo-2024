# Leitura dos primeiros valores
valor1 = input().split()
A = int(valor1[0])
B = int(valor1[1])

# Leitura dos segundos valores
valor2 = input().split()
C = int(valor2[0])
D = int(valor2[1])

# Cálculo da soma
soma = A * C + ((A // B) * D)

# Exibe o resultado
print(soma)
