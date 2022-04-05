a=input()
cripto="" 

for i in a: 
	if i == 'a' or i == 'A': 
		cripto += '@' 
	elif i == 'o' or i == 'O': 
		cripto += '*'
	else: 
		cripto += i 
cripto = cripto.lower() 
print(cripto)

