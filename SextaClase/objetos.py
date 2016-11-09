#######
# Objetos
#######

class Persona:
	#atributos de la clase
	edad=0
	genero=""
	nombre=""
	altura=0

	#metodos de la clase
	def caminar(self):
		print("Estoy caminando!!")

	def saludar(self):
		print("Hola!! soy %s"%self.nombre)

	def comer(self,comida):
		print("Me gusta ",comida)

	def cumpleaños(self):
		self.edad+=1

class Persona2(Persona):

	def __init__(self,nombre,edad,genero):
		self.nombre=nombre
		self.edad=edad
		self.genero=genero
		print("Se ha creado una persona ")		

class Persona3():

		def __init__(self,nombre,apellido,edad,genero,dinero):
			self.nombre=nombre
			self.apellido=apellido
			self.edad=edad
			self.genero=genero
			self.dinero=dinero
			print("Hola soy %s %s"%(self.nombre,self.apellido))
			print("Tengo $ ",self.dinero)

		def prestarDinero(self,persona,monto):
			if(self.dinero>=monto):
				persona.dinero+=monto
				self.dinero-=monto
			else:
				print("Ahorita no joven")







luis=Persona3("Luis","Torres",22,"M",100)
print("Dinero de Luis",luis.dinero)

pablo=Persona3("Pablo","Gonzales",33,"M",0)
print("Dinero de Pablo",pablo.dinero)
pablo.prestarDinero(luis,1000)

luis.prestarDinero(pablo,50)
print("Dinero de Luis",luis.dinero)
print("Dinero de Pablo",pablo.dinero)





#Instanciar una clase
juan=Persona()
alan=Persona2("alan",22,"M")
paco=Persona2("Paco",10,"M")
maria=Persona2("Maria",12,"F")
juan.edad=22
juan.genero="M"
juan.nombre="Juan"
juan.altura=2.2

juan.saludar()
Persona.saludar(juan)

print("Edad de Juan ",juan.edad)
juan.comer("tamales")
juan.cumpleaños()
print("Edad de Juan ",juan.edad)

alan.saludar()








