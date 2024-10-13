distancia = int(input("Digite a distância total percorrida (em Km): "))
combustivel = float(input("Digite o total de combustível gasto (em litros): "))

# Calcular o consumo médio
consumo_medio = distancia / combustivel

print(f"{consumo_medio:.3f} km/l")
