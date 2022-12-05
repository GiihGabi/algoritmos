peso = float(input(" digite aqui o peso "))
altura = float(input(" digite aqui a altura "))
IMC = peso / (altura * altura)

#se IMC < 18:
if IMC < 18:
  print("Você está abaixo do peso")
elif IMC >= 18 and IMC < 25:
  print("Peso normal")
elif IMC >= 25 and IMC < 30:
  print("Sobrepeso")
elif IMC >= 30 and IMC < 35:
  print("Obesidade de 1º grau")
elif IMC >= 35 and IMC < 40:
  print("Obesidade de 2º grau")
else:
  print("Obesidade de 3º grau")