import math
#Pedimos las tres variables
a=int(input("ingresa coeficiente cuadratico:\n"))
b=int(input("ingresa coeficiente lineal:\n"))
c=int(input("ingresa constante:\n"))
#Calculamos el discriminante
disc=b*b-4*a*c
#calculamos las dos raices
#Si estas son imaginarias nos va a dar un error de dominio
x1=(-b+(math.sqrt(disc)))/(2*a)
x2=(-b-(math.sqrt(disc)))/(2*a)
#Imprimimos el resultado
print("X1 = "+str(x1)+" X2 = "+str(x2))
