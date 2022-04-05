palitos = [int(item) for item in input().split()]
palpites = [int(item) for item in input().split()]
soma = 0
for item in palitos:
  soma += item 
ganhou = -2
for item in palpites:
  if item == soma:
    ganhou = palpites.index(item)
print(ganhou +1)
