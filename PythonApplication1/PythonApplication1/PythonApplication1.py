a=input()
i=0
size=int(len(a))
while i<size/2:
	if a[i]!=a[size-i-1]:
		print('Строка - не полиндром')
		exit()
	i+=1
print('Строка - полиндром')