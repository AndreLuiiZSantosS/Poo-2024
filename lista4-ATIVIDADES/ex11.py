while True:
    try:
        n, r = map(int, input().split())
        mergulhos = list(map(int, input().split()))
        
        todos_mergulhadores = set(range(1, n + 1))
        mergulhadores_voltaram = set(mergulhos)
        
        faltantes = todos_mergulhadores - mergulhadores_voltaram
        
        if faltantes:
            print(" ".join(map(str, sorted(faltantes))))
        else:
            print("*")
    
    except EOFError:
        break
