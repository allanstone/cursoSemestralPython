########
## Lambdas
########

cubo = lambda x : x**3

print(cubo(3))
print(cubo(5))
print(cubo(7))

lista=[0,1,2,3,4,5,6]

cubos=map(cubo,lista)

print(list(cubos))

def cuadrado(x):
	return x**2

print(list(map(cuadrado,list(map(cuadrado,lista)))))

lista3=filter(lambda n: n%2==0,lista)
print(list(lista3))

import functools

a=functools.reduce(lambda a,b : a+b,lista)
print(a)



