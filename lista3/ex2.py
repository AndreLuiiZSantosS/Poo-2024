a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))
c = int(input("Digite o terceiro valor: "))

maior_ab = (a + b + abs(a - b)) // 2

maior = (maior_ab + c + abs(maior_ab - c)) // 2

print(f"{maior} eh o maior")
