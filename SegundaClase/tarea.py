import math
a=int(input("ingresa coeficiente cuadratico\n"))
b=int(input("ingresa coeficiente lineal\n"))
c=int(input("ingresa constante\n"))
disc=b*b-4*a*c

x1=(-b+(math.sqrt(disc)))/(2*a)
x2=(-b-(math.sqrt(disc)))/(2*a)
print("X1 = "+str(x1)+" X2 = "+str(x2))
