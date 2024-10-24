class ContaBancaria:
  def __init__(self, titular, numero_conta, saldo=0):
    self.titula = titular
    self.numero_conta = numero_conta
    self.saldo = saldo

  def depositar(self, valor):
    self.saldo += valor
    print(f"Deposito de R${valor:.2f} realizado com sucesso. Saldo atual: R${self.saldo:.2f}")

  def sacar(self, valor):
    if valor > self.saldo:
      print("Saldo Insuficiente")
    else:
      self.saldo -= valor
        print(f"Saldo de R${valor:.2f} sacado com sucesso. Saldo atual: R${self.saldo:.2f}")

if __name__ == __main__:
    titular = input("Digite o nome do titular da conta: ")
    numero_conta = input("Digite o número da conta: ")
    saldo_inicial = float(input("Digite o saldo inicial da conta: "))
    
    conta = ContaBancaria(titular, numero_conta, saldo_inicial)
      while True:
        print("\nMenu:")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Saldo")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
          valor = float(input("Digite o valor a ser depositado: "))
          conta.depositar(valor)
        elif opcao == "2":
          valor = float(input("Digite o valor a ser sacado: "))
          conta.sacar(valor)
        elif opcao == "3":
          print(f"Saldo atual: R${conta.saldo:.2f}")
        elif opcao == "4":
          print("Saindo do programa.")
          break
        else
          print("Opção inválida. Tente novamente.")
  

      
    
    
    
      