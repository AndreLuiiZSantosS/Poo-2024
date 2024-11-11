while True:
    try:
        n = int(input())
        botas = {}
        
        for _ in range(n):
            tamanho, lado = input().split()
            if tamanho not in botas:
                botas[tamanho] = {'D': 0, 'E': 0}
            botas[tamanho][lado] += 1
        
        pares = 0
        for tamanho in botas:
            pares += min(botas[tamanho]['D'], botas[tamanho]['E'])
        
        print(pares)
    
    except EOFError:
        break
