def maior (x, y):
  return x if x > y else y

num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero: "))

print("O maior numero é:"), maior(num1, num2)
