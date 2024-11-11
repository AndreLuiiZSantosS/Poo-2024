n = int(input())
fila_original = list(map(int, input().split()))
saidas = list(map(int, input().split()))

for s in saidas:
    if s in fila_original:
        fila_original.remove(s)

print(" ".join(map(str, fila_original)))
