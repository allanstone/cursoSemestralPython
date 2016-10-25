#########
#  Listas
#########

cadena="alan"
print(type(cadena))
lista=[]
print(type(lista))

numeros=[1,2,3,4,5]
print(numeros[2])
print(cadena[2])

numeros[2]=10
print(numeros[2])

#cadena[2]='z'
nuevaLista=[123,545.324,numeros,"hola",True]
print(nuevaLista)

nuevaLista[2][2]=3
print(nuevaLista)


lenguajes=["python","java","c++","perl","ruby"]

#for x in range(0,len(lenguajes)):
#	print(lenguajes[x])

for lenguaje in lenguajes:
	print(lenguaje)

acum=0
for num in numeros:
	acum+=num
	#Recordar que es lo mismo que acum=num+acum
print("Acumulador: ",acum)


#acum[0]=0
#SLICING
print(lenguajes[:])

letras=["a","b","c","d"]
letras.append("e")
print(letras)
#letra=letras.pop()
##print(letra)+
#letras.pop()
#letras.pop()
#letras.pop()
#letras.pop()
#letras.pop()
#letras.pop()
print(letras)

a="A"
#print([a]+letras)
print(list(a)+letras)

#insertar en un indice especificado
letras.insert("P",0)

















