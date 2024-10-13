while True:
  # Lê a frase
  frase = input().strip()

  # Verifica se a entrada é o asterisco que encerra os casos
  if frase == '*':
      break

  # Divide a frase em palavras
  palavras = frase.split()

  # Obtém a primeira letra da primeira palavra e a converte para minúscula
  primeira_letra = palavras[0][0].lower()

  # Verifica se todas as palavras começam com a mesma letra (ignorando maiúsculas e minúsculas)
  tautograma = all(palavra[0].lower() == primeira_letra for palavra in palavras)

  # Imprime 'Y' se for tautograma, 'N' caso contrário
  if tautograma:
      print('Y')
  else:
      print('N')
