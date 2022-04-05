letra = input()
troca = input()
msg = str(input())
nova_msg = ""

for i in msg:
  if i != letra:
    nova_msg += i
  else:
    nova_msg+=troca


print(nova_msg)