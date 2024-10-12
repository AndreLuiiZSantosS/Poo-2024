# Ler as notas dos bimestres
nota_1 = int(input("Digite a nota do primeiro bimestre da disciplina: "))
nota_2 = int(input("Digite a nota do segundo bimestre da disciplina: "))

# Definir os pesos
peso_1 = 2
peso_2 = 3

# Calcular a média parcial
media_parcial = (nota_1 * peso_1 + nota_2 * peso_2) / (peso_1 + peso_2)

# Mostrar a média parcial
print(f"Média parcial = {media_parcial:.0f}")