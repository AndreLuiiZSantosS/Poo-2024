# Função para ler e validar uma nota
def ler_nota():
    while True:
        nota = float(input())
        if 0 <= nota <= 10:
            return nota
        else:
            print("nota invalida")

# Lendo as duas notas válidas
nota1 = ler_nota()
nota2 = ler_nota()

# Calculando a média
media = (nota1 + nota2) / 2

# Exibindo a média com duas casas decimais
print(f"media = {media:.2f}")
