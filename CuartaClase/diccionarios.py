#######
## Diccionarios
#######
valor=5
d={"llave":valor,"llave2":valor+1,"llave3":valor,"llave":valor+10}

print(d)

elementos={"O":"OXIGENO","H":"HELIO","AU":"ORO"}
elementos["C"]="CARBONO"
print(elementos)

telefonos={
#"nombre":["appellido","telefono",edad,"correo"],
"alan":["garrido","55141234",22,"allanstone@gmail.com"],
"juan":["nieve",None,13,"jonsnow@westeros.com"],
"pepe":["lopez","342342",23,"pepe@pepe.pepe"]
}
print(telefonos["alan"][0])
telefonos["esteban"]="me cae mal"
print(telefonos["esteban"])
del telefonos["esteban"]
#print(telefonos["esteban"])

for x,y in elementos.items():
	print("Símbolo: ",x," Nombre: ",y)
print("####Mi directorio telefonico######")
for key in sorted(telefonos.keys()):
	print("\tNombre: ",key)
	print("\tApellido: ",telefonos[key][0])
	print("\tTelefono: ",telefonos[key][1])
	print("\tEdad: ",telefonos[key][2])
	print("\tCorreo: ",telefonos[key][3])









