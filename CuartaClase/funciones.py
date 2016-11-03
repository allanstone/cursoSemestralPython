########
### Funciones
########

def funcionpordefinir(a,b,c):
	pass #recordar implementar esto

def suma(a,b):
	return a+b
a=1
b=11
c=3
d=4
e=5
print(suma(a,b))

def suma2(a,b=0):
	return a+b

def suma3(a=0,b=0,*variables):
	acum=0
	for x in variables:
		acum+=x
	return acum+a+b
'''
#print(suma(a))
print(suma3())
print(suma3(a))
print(suma3(a,b))
print(suma3(a,b,c))
print(suma3(a,b,c,d))
print(suma3(a,b,c,d,e,4,6,7,7,8,9,0,0,3,5))
'''
#print(suma(a))
print(suma2(a))
print(suma2(b=3,a=4))

#fact 3!=3*2*1

def fact(n):
	res=1
	for x in range(1,n+1):
		#res*=x
		res=res*x
	return res
"""
print("El factorial de 0: ",fact(0))
print("El factorial de 1: ",fact(1))
print("El factorial de 2: ",fact(2))
print("El factorial de 3: ",fact(3))
print("El factorial de 5: ",fact(5))
"""
#5!= 5*4!
def factRec(n):
	if n==0 or n==1:
		return 1
	else:
		return n*factRec(n-1)
0 1 1 2 3 5 8 13 21
print("El factorial de 0: ",factRec(0))
print("El factorial de 1: ",factRec(1))
print("El factorial de 2: ",factRec(2))
print("El factorial de 3: ",factRec(3))
print("El factorial de 5: ",factRec(5))
print("El factorial de 1000: ",factRec(1000))