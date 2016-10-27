##############################################
#Programa diseñado para el cálculo del índice de masa corporal
##############################################

from math import *
import os

print ("¡Hola! Este es un programa que calcula el índice de masa corporal")
while True:
	VAR=0
	a=float(input("Dame tu altura (en metros) : "))
	p=float(input("Dame tu peso (en kilogramos) : "))
	IMC=p/(a**2)
	print ("Tu IMC es: ",IMC)
	if IMC<=18.5:
		print("Tienes bajo peso")
	elif IMC>18.5 or IMC<=24.99:
		print("Tienes peso normal")
	elif IMC>24.99 or IMC<=30:
		print("Tienes sobrepeso")
	else:
		print("Tienes obesidad")
	while VAR==0:
		B=input("¿Quieres calcularlo de nuevo? (S/N)")
		if B=="N":
			VAR=1
		elif B=="S":
			VAR=2
		else:
			print ("Selecciona una de las opciones disponibles")
	if VAR==1:
		os.system('cls')
		break
	os.system('cls')
		
