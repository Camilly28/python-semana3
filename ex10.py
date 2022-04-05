texto =  [str(i) for i in input().split()]
mico = texto.count('@')
if mico >= 1:
  print('mico!')
else:
  print('sem mico')
