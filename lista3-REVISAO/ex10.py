import math

# Função para verificar se um número é primo
def eh_primo(x):
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    limite = int(math.sqrt(x)) + 1
    for i in range(3, limite, 2):
        if x % i == 0:
            return False
    return True

# Leitura do número de casos de teste
N = int(input())

# Para cada caso de teste
for _ in range(N):
    # Lê o valor inteiro X
    X = int(input())

    # Verifica se X é primo e imprime o resultado
    if eh_primo(X):
        print("Prime")
    else:
        print("Not Prime")
