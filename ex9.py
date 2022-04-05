nome = str(input())
texto =  [str(i) for i in input().split()]

mico = texto.count('mico')
if mico >= 1:
  print(nome,'mico!')
else:
  print(nome,'ok')

