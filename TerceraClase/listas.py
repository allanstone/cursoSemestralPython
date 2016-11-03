#########
#  Listas
#########

#Son tipos de datos llamados colecciones, porque contienen otros tipos de datos y aparte a si mismos
lista=[]
print(type(lista))
#Son diferentes a las cadenas ya que si soportan asignación por elemento

cadena="alan"
print(type(cadena))

#Las cadenas no soportan este tipo de asignaciones
#cadena[0]="A"

numeros=[1,2,3,4,5]
#Pero si se pueden acceder a los elementos
print(numeros[2])
print(cadena[2])

#Las listas se puede modificar uno de ellos
numeros[2]=10
print(numeros[2])

#Podemos usar cualquier objeto dentro de estas incluso otras listas
nuevaLista=[123,545.324,numeros,"hola",True]
print(nuevaLista)

#Accedemos a la lista interna desde la externa de esta manera
nuevaLista[2][2]=3
print(nuevaLista)

#Las listas son bastante expresivas
lenguajes=["python","java","c++","perl","ruby"]

#Y podemos recorrerlas de estas dos maneras
#for x in range(0,len(lenguajes)):
#	print(lenguajes[x])
#Con un ciclo for each se usa una variable temporal que solo es utilizable desde el ciclo
for lenguaje in lenguajes:
	print(lenguaje)

#Y podemos usarla para realizar operaciones
acum=0
for num in numeros:
	acum+=num
	#Recordar que es lo mismo que acum=num+acum
print("Acumulador: ",acum)

#Utilizar objetos que no son indexables con esta notación causará un error
#acum[0]=0

#SLICING
#Obtiene una porción de la lista... nombreLista[inicio:fin-1:paso]
#Se parece mucho a como usamos el range()
#Si no se tienen los indices se toma el resto por omisión
print(lenguajes[:])

letras=["a","b","c","d"]
#Agregamos a la lista con append al final
letras.append("e")
print(letras)
#Y sacamos el último que entró con pop
letra=letras.pop()
print(letra)
#Si no se asigna a una variable se pierde el valor
#letras.pop()
#letras.pop()
#letras.pop()
#letras.pop()
#letras.pop()
#letras.pop()
#Si se hace pop de una lista vacia se genera un error
print(letras)

a="A"
#Las listas soportan concatenación y tambíén se puede castear un objeto a una lista
#print([a]+letras)
print(list(a)+letras)

#insertar en un indice especificado
letras.insert("P",0)
print(letras)

















