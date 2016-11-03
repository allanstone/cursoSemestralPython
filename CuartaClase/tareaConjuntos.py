#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Operaciones con conjuntos
'''
l1=[]
l2=[]
while True:
	a=input("Agregar elemento a la lista?: ")
	l1.append(a)
	pregunta=input("Escribe enter para salir")
	if pregunta=="":
		break
c1=set(l1)
while True:
	a=input("Agregar elemento a la lista2?: ")
	l2.append(a)
	pregunta=input("Escribe enter para salir")
	if pregunta=="":
		break
c2=set(l2)
print(c1)
print(c2)
'''
c1=set()
dato=1
while dato!=0:
	dato=int(input("Dame un entero para el conjunto o cero para salir: "))
	c1.add(dato)
c2=set()
dato=1
while dato!=0:
	dato=int(input("Dame un entero para el conjunto o cero para salir: "))
	c2.add(dato)

#interseccion
print(c1&c2)
#union
print(c1|c2)
#diferencia
print(c2-c1)
#diferencia simetrica
print(c2^c1)
#subconjunto si son iguales regresa false
print(c2>c1)
#subconjunto si son iguales regresa true
print(c2=>c1)






