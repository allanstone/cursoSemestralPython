#from docu import fib

import docu as f

f.fib(4)

print(dir(f))

print("Ruta del modulo",f.__file__)
print("Nombre del modulo",f.__name__)
print("Documentacion del modulo",f.__doc__)
print("Nombre que se le puso al modulo",f.__module__)
print("Nombre del autor: ",f.__author__)
print("Derechos de autor: ",f.__copyright__)
print("Documentacion de la funcion: ",f.fib.__doc__)
