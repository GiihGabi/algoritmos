idade = int(input("escreva aqui a idade do nadador"))

#se idade <= 8 então: 
if idade <= 8:
  print("categoria infantil A")
elif idade < 13:
  print("categoria infantil B")
elif idade < 18:
  print("categoria infantil A")
elif idade < 21:
  print("categoria infantil B")
elif idade >= 21:
  print("categoria sênior")