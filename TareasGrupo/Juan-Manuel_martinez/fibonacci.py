##Serie de Fibonacci. Esta serie se forma de la siguiente manera:
#a1=1
#a2=1
#a3=2
#an=a(n-1)+a(n-2) para n>=3

#Una primera forma de hacerla sería

n=int(input("Dame el numero: "))

def fibonacci(n):

	if n==0:
		return 0
	elif n==1:
		return 1
	else:
		return(fibonacci(n-1)+fibonacci(n-2))
print(fibonacci(n))

#Una segunda forma sería

#n=int(input("Dame el numero de la serie: "))

#def fibonacci(n):
#	print("fibonacci: "+ str(n))
#	if n<2:
#		return n
#	else:
#		return(fibonacci(n-1)+fibonacci(n-2))
#print(fibonacci(n))



