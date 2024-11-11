while True:
    try:
        n, m = map(int, input().split())
        matriz = []
        
        for _ in range(n):
            linha = list(map(int, input().split()))
            matriz.append(linha)
        
        resultado = [[0] * m for _ in range(n)]
        
        for i in range(n):
            for j in range(m):
                if matriz[i][j] == 1:
                    resultado[i][j] = 9
                else:
                    soma = 0
                    for x, y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                        nx, ny = i + x, j + y
                        if 0 <= nx < n and 0 <= ny < m and matriz[nx][ny] == 1:
                            soma += 1
                    resultado[i][j] = soma
        
        for linha in resultado:
            print(' '.join(map(str, linha)))
    
    except EOFError:
        break
