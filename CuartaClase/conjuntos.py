###########
##Conjuntos
###########

#Parecidos a las tuplas pero sin elementos repetidos
numeros={1,2,2,3,4}
print(type(numeros))
#Podemos crearlos apartir de una tupla
numeros2=set((1,4,10,3))

#Operaciones con conjuntos
print(numeros-numeros2)
print(numeros|numeros2)
print(numeros&numeros2)



#longitud del conjunto
len({'azul', 'verde', 'rojo'})

#x in s permite saber si el elemento x está en el conjunto s:

print(3 in {2, 3, 4})

#x not in s permite saber si x no está en s:

print(10 not in {2, 3, 4})

#s.add(x) agrega el elemento x al conjunto s:

s = {6, 1, 5, 4, 3}.add(-37)

print(s)

#s.remove(x) elimina el elemento x del conjunto s:

s = {6, 1, 5, 4, 3}.remove(1)
print(s)

#& y | son, respectivamente, los operadores de intersección y unión:

a = {1, 2, 3, 4}
b= {2, 4, 6, 8}
print(a&b)
print(a&b)

#s - t entrega la diferencia entre s y t; es decir, los elementos de s que no están en t:
print(a-b)

#s ^ t entrega la diferencia simétrica entre s y t; es decir, los elementos que están en s o en t, pero no en ambos:
print(a ^ b)
#El operador < aplicado sobre conjuntos significa «es subconjunto de»:

print({1, 2} < {1, 2, 3})

#s <= t también indica si s es subconjunto de t. La distinción ocurre cuando los conjuntos son iguales:

