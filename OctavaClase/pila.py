class Pila():
	
	def __init__(self):
		self.st=-1
		self.pila=[]

	def pop(self):
		if self.vacia():
			return None
		else:
			self.st-=1
			return self.pila.pop()
	def push(self,elemento):
		self.st+=1
		self.pila.append(elemento)

	def peek(self):
		print(self.pila[self.st])

	def vacia(self):
		if self.pila:
			return False
		return True

	def __str__(self):
		return "Pila: "+str(self.pila)

p=Pila()
print("La pila esta vacia?: ",p.vacia())
print("Pop de pila vacia ",p.pop())
p.push("a")
p.push("b")
p.push("c")
p.push("d")
print("La pila esta vacia?: ",p.vacia())
print("Pop de pila: ",p.pop())
print(p)
p.peek()











