timeA = str(input())
timeB = str(input())
pontoA = [int(i)  for i in input().split()]
pontoB = [int(i)  for i in input().split()]

tamanho = len(pontoA)
set1 = 0 #time a
set2 = 0 #time b

for i in range(tamanho):
  if pontoA[i] > pontoB[i]:
    set1 += 1
  elif pontoB[i]>pontoA[i]:
    set2 += 1

    
if set1 > set2:
  print(timeA,'(total',tamanho,'sets)')
elif set2 > set1:
  print(timeB,'(total',tamanho,'sets)')
