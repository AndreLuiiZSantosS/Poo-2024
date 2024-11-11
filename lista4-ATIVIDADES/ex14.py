while True:
    try:
        n = int(input())
        numeros = []

        for _ in range(n):
            numero = float(input())
            numeros.append(numero)

        numeros.sort(reverse=True)

        for num in numeros:
            print(f"{num:.2f}")
    
    except EOFError:
        break
