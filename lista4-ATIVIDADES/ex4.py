vetor = []
for i in range(100):
    num = float(input())
    vetor.append(num)
    if num <= 10:
        print(f"A[{i}] = {num:.1f}")
