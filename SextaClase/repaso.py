#####
# Repaso
#####

entero=12312312
enteroN=-121
numerote=12312319342809479837985730847508374058734057380475083475304875038475

i=0
#while(True):
#	i+=1
#	if(i<0):
#		break
print(i)

flotante=entero/enteroN
print("{0:0.2f}".format(flotante))


cmplx=1+2j
cmplx2=2+4j
print(cmplx)
print(type(cmplx))
print(cmplx+cmplx2)
print(cmplx*cmplx2)

cadena="asdfa"
cadena2='asdf'
cadena3="""Hola"""

conca=cadena+cadena2+cadena3
mult=cadena*3
print(mult)

cadenaCruda=r"hola \n"
print(cadenaCruda)


print("La cadena 1 es: %s La cadena cruda es: %s" % (cadena,cadenaCruda))


lista=[1,2,3,4,5]
for i in range(0,len(lista)):
	lista[i]+=1

print(lista)
print(list(map(lambda a:a+1,lista)))


print(lista[1:4])
print(lista[-1])
print(lista[::-1])

listaR=lista[::-1]
for i in range(0,len(listaR)):
	listaR[i]+=1
print(lista)
print(listaR)










