
peso = float(input("Dame tu peso en kg  "))
altura = float(input("Dame tu altura en metros  "))

imc = peso / (altura**2)

if imc < 18.5:
	print("Peso bajo, acude a tu médico: ", imc)
elif 18.5 <= imc < 25:
	print("Peso adecuado, bien hecho campeón: ", imc)
elif 25 <= imc < 30:
	print("Tienes sobrepeso mi chavo: ", imc)
elif 30 <= imc:
	print("Alerta, tienes obesidad: ", imc)