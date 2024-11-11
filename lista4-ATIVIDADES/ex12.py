c, n = map(int, input().split())
vagas_ocupadas = 0
placas_estacionadas = set()
ganhos = 0

for _ in range(n):
    operacao, placa, comprimento = input().split()
    comprimento = int(comprimento)

    if operacao == 'C':  # Chegada
        if vagas_ocupadas + comprimento <= c:
            if placa not in placas_estacionadas:
                vagas_ocupadas += comprimento
                placas_estacionadas.add(placa)
                ganhos += 10  # Ganha R$10 por carro estacionado
        else:
            print("Capacidade insuficiente")
    
    elif operacao == 'S':  # Saída
        if placa in placas_estacionadas:
            vagas_ocupadas -= comprimento
            placas_estacionadas.remove(placa)

print(ganhos)
