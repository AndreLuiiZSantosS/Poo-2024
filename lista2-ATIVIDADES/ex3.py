class ContaBancaria:
  def __init__(self, nome_titular, numero_conta, saldo = 0.0):
    self._nome_titular = nome_titular
    self._numero_conta = numero_conta
    self._saldo = saldo

  def depositar(self, valor):
    if valor > 0:
      salf._saldo += valor

  def sacar(self, valor):
    if 0 < valor <= self._saldo:
      self._saldo -= valor

  def obter_saldo(self)
    return self._saldo

conta = ContaBancaria("Andre Luiz", 12345678, 1000)
conta.depositar(500)
conta.sacar(200)
print("saldo:", conta.obter_saldo())
