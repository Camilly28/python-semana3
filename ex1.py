saida = 'ok'

proibido = ['a','e','i','o','u',' ']

entrada = input()

if len(entrada) != 11:
  saida = 'erro: tamanho inválido'
else:
  for letra in entrada:
    if letra in proibido:
      saida = 'erro: caractere inválido'
      break
print(saida)
