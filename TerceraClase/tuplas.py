#######
# Tuplas
#######

#Las tuplas son como las listas pero con la característica de inmutabilidad
#de las cadenas

tupla=("a",1,True)
print(type(tupla))

lista=list(tupla)
print(type(lista))

#Se puede acceder a un elemento de esta
print(tupla[1])
#Pero no soportan asignación por elemento
#tupla[2]=False

a=1
b=2
#Se pueden crear apartir de variables de la siguente manera
t2=a,b
a=3
print(t2)

#Pueden contener otras tuplas o listas
t3=(tupla,t2,lista)
print(t3)
#La lista si soporta asignación por elemento
t3[2][0]=4

print(t3)
#Tupla vacia
vacia=()
#Tupla de un solo elemento
singleton=a,
print(type(vacia),len(vacia))
print(type(singleton),len(singleton))

#Empaquetado de datos en una tupla
t4=(1,2,4)
#Desempaquetado de datos en variables
a,b,c=t4
print(a,b,c)


###Conjuntos

#Parecidos a las tuplas pero sin elementos repetidos
numeros={1,2,2,3,4}
print(type(numeros))
#Podemos crearlos apartir de una tupla
numeros2=set((1,4,10,3))

#Operaciones con conjuntos
print(numeros-numeros2)
print(numeros|numeros2)
print(numeros&numeros2)
