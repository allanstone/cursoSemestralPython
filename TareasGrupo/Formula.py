#Programa para calcular las raíces de un polinomio de segundo grado usando la formula general

from math import *

print("Hola, este es un programa para calcular raíces, dame el valor de los coeficientes de tu polinomio")
a=int(input("Dame el coeficiente del primer término: "))
b=int(input("Dame el coeficiente del segundo término: "))
c=int(input("Dame el coeficiente del tercer término: "))
x1=(-b+sqrt(b**2-4*a*c))/(2*a)
x2=(-b-sqrt(b**2-4*a*c))/(2*a)
print("La primer raíz es: ")
print(x1)
print("La segunda raíz es: ")
print(x2)