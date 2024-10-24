# Ler o valor
valor = int(input("Digite o valor: "))

# Inicializar variáveis
troco = valor

# Calcular o número de notas de cada valor
cem = troco // 100
troco -= cem * 100

cinquenta = troco // 50
troco -= cinquenta * 50

vinte = troco // 20
troco -= vinte * 20

dez = troco // 10
troco -= dez * 10

cinco = troco // 5
troco -= cinco * 5

dois = troco // 2
troco -= dois * 2

# O restante é o número de notas de R$ 1,00
um = troco

# Mostrar os resultados
print(f"{valor}")
print(f"{cem} nota(s) de R$ 100,00")
print(f"{cinquenta} nota(s) de R$ 50,00")
print(f"{vinte} nota(s) de R$ 20,00")
print(f"{dez} nota(s) de R$ 10,00")
print(f"{cinco} nota(s) de R$ 5,00")
print(f"{dois} nota(s) de R$ 2,00")
print(f"{um} nota(s) de R$ 1,00")
