import math

while True:
    try:
        # Leitura de cada caso de teste
        D, VF, VG = map(int, input().split())

        # Calcula o tempo do ladrão para percorrer 12 milhas
        tempo_ladrao = 12 / VF

        # Calcula a distância que a guarda costeira precisa percorrer (hipotenusa)
        distancia_guarda = math.sqrt(D**2 + 12**2)

        # Calcula o tempo da guarda costeira para percorrer essa distância
        tempo_guarda = distancia_guarda / VG

        # Verifica se a guarda costeira consegue interceptar o ladrão
        if tempo_guarda <= tempo_ladrao:
            print("S")
        else:
            print("N")
    except EOFError:
        break
