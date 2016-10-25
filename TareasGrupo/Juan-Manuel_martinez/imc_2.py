##Este programa calcula el indice de masa corporal a partir de proporcionar
##el peso y la altura
##Si se dan valores negativos o iguales a cero del peso y de la altura
## el programa volvera a solicitar el dato hasta que se introduscan valores 
## positivos y mayores a cero.


peso=float(input("Proporciona tu peso en (Kg): "))
altura=float(input("Proporciona tu altura en (m): "))
while peso<=0 or altura<=0:
	peso=float(input("Proporcina tu peso en (Kg): "))
	altura=float(input("Proporciona tu altura: "))

imc=peso/altura**2

print ("El peso es: ",peso)
print ("La altura es: ",altura)
print("tu índice de masa corporal es: IMC= {0:.3f}".format(imc))

if imc<16:
	print ("Presentas delgadez extrema")
elif imc>=16 and imc<=16.99:
	print ("Presentas delgadez moderada")
elif imc>16.99 and imc<=18.49:
	print ("Presentas una leve delgadez")
elif imc>18.49 and imc<=24.99:
	print ("Estas normal")
elif imc>24.99 and imc<=29.99:
	print ("Presentas sobre peso")
elif imc>29.99 and imc<=34.99:
	print ("Presentas obesidad leve")
elif imc>34.99 and imc<=39.99:
	print ("Presentas obesidad media")
elif imc>=40:
	print ("Presentas obesidad mórbida")

