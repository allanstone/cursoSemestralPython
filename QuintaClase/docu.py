"""Este modulo nos ayuda a usar la funcion de fibonacci"""
######
## Documentacion
######

__module__="Fibonacci"
__author__="Alan Garrido"
__copyright__="Copyright Proteco 2016"

def fib(n):
	'''Esta funcion imprime la serie de fibonnaci hasta n'''
	a,b=0,1
	while b<n:
		print(b,end=" ")
		a,b=b,a+b
	print()