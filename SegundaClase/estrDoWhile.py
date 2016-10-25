#######
# Do while loop
#######

#Este ciclo lo implementamos con un ciclo infinito
#Necesitamos hacer por lo menos una vez el código
while True:
	#Escribimos la parte de código que queremos que se haga al menos una vez
	print("Hazlo al menos una vez!!")
	#Preguntamos por una condición que nos haga salir del ciclo
	if int(input("escribe cero para salir: "))==0:
		break
	#Muy importante que no pongan sentencias break
	#fuera de ciclos ya que les marcará un error
