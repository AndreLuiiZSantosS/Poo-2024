t = int(input())  # Número de casos de teste

for _ in range(t):
    n = int(input())  # Número de carneiros
    carneiros = list(map(int, input().split()))
    
    # Usando set para remover duplicatas e contar os distintos
    distintos = len(set(carneiros))
    print(distintos)
