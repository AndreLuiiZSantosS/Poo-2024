import math

# Ler a base e a altura do retângulo
base = float(input("Digite a base do retângulo: "))
altura = float(input("Digite a altura do retângulo: "))

# Calcular a área
area = base * altura

# Calcular o perímetro
perimetro = 2 * (base + altura)

# Calcular a diagonal
diagonal = math.sqrt(base**2 + altura**2)

# Mostrar os resultados com duas casas decimais
print(f"Área = {area:.2f} - Perímetro = {perimetro:.2f} - Diagonal = {diagonal:.2f}")
