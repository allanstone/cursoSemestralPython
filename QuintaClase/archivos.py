########
#  Archivos
########

#Un archivo se trata como cualquier otro objeto de python
#para abrirlo se usa la función open que recibe el nombre
#o la ruta del archivo y un modo de apertura
archivo = open("archivo.txt","a+")
#Un archivo tiene diferentes propiedades
print("Nombre del archivo: ",archivo.name)
print("Modo: ",archivo.mode)
#Podemos verificar si se encuentra abierto o cerrado
#archivo.close()
if archivo.closed:
	print("El archivo esta cerrado")
else:
	print("El archivo esta abierto")
#Por buenas prácticas de programación siempre se deben cerrar los
#archivos o cualquier flujo de datos 

#Para insertar datos en un archivo se puede usar la función write
texto="hola"#input("Ingresa lo que quieras agregar al archivo: ")
archivo.write(texto)

#Para leer denuevo el archivo hay que mover el apuntador interno
#a la posición relativa del inicio de archivo
archivo.seek(0)

#Para leer el archivo completo con todo y los saltos de linea
print(archivo.read())

archivo.close()

#Forma más simple de abrir un archivo, al final del bloque se cierra
#automaticamente y todo lo maneja con la referencia de f
with open("archivo.txt") as f:
	#Readlines regresa una lista con cada una de las lineas con los \n al final
	lineas=f.readlines()

#la función rstrip nos puede ayudar a quitar ese salto de línea
#investigar como se hace para la tarea
print(lineas)