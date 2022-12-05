valorcompra = float(input("escreva aqui o valor da compra "))

#se desconto >= 500 então:
if valorcompra >= 500:
  desconto = (valorcompra * 0.25)
  total = (valorcompra - desconto)
elif valorcompra >= 200:
  desconto = (valorcompra * 0.20)
  total = (valorcompra - desconto)
elif valorcompra < 200:
  desconto = (valorcompra * 0.15)
  total = (valorcompra - desconto)

print(f"desconto: {valorcompra * 0.20}")
print(f"total: {valorcompra - desconto}")