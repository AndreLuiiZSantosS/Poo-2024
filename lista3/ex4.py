import math

# Ler os valores de ponto flutuante para os pontos p1 e p2
x1, y1 = map(float, input("Digite as coordenadas do ponto p1 (x1 y1): ").split())
x2, y2 = map(float, input("Digite as coordenadas do ponto p2 (x2 y2): ").split())

# Calcular a distância entre os pontos
distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Mostrar o resultado com 4 casas decimais
print(f"{distancia:.4f}")
