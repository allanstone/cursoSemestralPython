##############################################
# Calculadora de conjuntos
##############################################

import os

os.system('cls')
print("Esta es una calculadora de conjuntos")
while True:
	print("Los conjuntos se deben de ingresar separando cada elemento con un espacio. Ej. 1 2 3")
	res1=input("Ingresa tu primer conjunto: ")
	res2=input("Ingresa tu segundo conjunto: ")
	a=set(res1.split(" "))
	b=set(res2.split(" "))
	print("¿Qué operación deseas utilizar?")
	print("1-Unión")
	print("2-Intersección")
	print("3-Diferencia")
	sup=False
	while sup==False:
		res=input(" ")
		if res=="1":
			#Unión
			union=a | b
			print("La unión es: ",union)
			sup=True
		elif res=="2":
			#Intersección
			inter=a & b
			print("La intersección es: ",inter)
			sup=True
		elif res=="3":
			#diferencia
			dif=a - b
			dif2= b - a
			print("La diferencia es: ",dif," U ",dif2)
			sup=True
		else:
			print("Por favor seleccione una de las opciones disponibles")
	sup2=False
	print("¿Desea realizar una nueva operación?(S/N)")
	while True:
		res3=input(" ")
		if res3=="S":
			break
		elif res3=="N":
			sup2=True
			break
		else:
			print("Por favor seleccione una de las opciones disponibles")

	if sup2==True:
		os.system('cls')
		break








