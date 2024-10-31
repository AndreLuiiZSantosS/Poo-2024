def iniciais(nome):
  return ''.join([palavra[0].upper() for palavra in nome.split()])

nome_completo = input("Digite seu nome completo: ")

print("iniciais: "), iniciais(nome_completo))
