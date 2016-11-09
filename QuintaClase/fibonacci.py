#Fibonacci interativo
def fib(n):
    a,b = 1,1
    for i in range(n-1):
        a,b = b,a+b
    return a

#print (fib(2))

#Fibonacci recursivo  Complejidad: O(2**n) 
def fiboRecu(n):
    if n==0:     #Primer caso base
        return 0
    elif n==1:   #Segundo caso base
        return 1 #no hace falta el else:
    return fiboRecu(n-1)+fiboRecu(n-2) #Recursividad


#print(fiboRecu(3))
#print(fiboRecu(500)) 

#Fibonacci matematico
from math import *
def fibomath(n):
    return((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))

#print(fibomath(3))
#print(fibomath(4)) #aqui empieza a variar presicion
#print(fibomath(5)) 

#Fibonacci by Keisuke
def fibonacci(n):
    lista=[0,1]
    while len(lista) < n:
        lista += [lista[len(lista)-1]+lista[len(lista)-2]]
    return lista

#regresa la lista de n fibonacci's
#print(fibonacci(1))
#print(fibonacci(4))
#print(fibonacci(6))

#Fibonacci memoization(tecnica computacional para guardar llamadas sucesivas a una funcion)
def memoize(fn, arg):
 memo = {}
 if arg not in memo:
  memo[arg] = fn(arg)
  return memo[arg]

#Regresa el sexto elemento de la serie
if __name__ == '__main__': 
  fibm = memoize(fib,5)
  print(fibm)

  fibm2 = memoize(fib,500)
  print(fibm2)