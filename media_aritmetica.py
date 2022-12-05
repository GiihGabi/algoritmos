count = 0
soma = 0
while(count < 5):
  valor = int(input("valor inteiro: "))
  soma = soma + valor 
  count = count + 1 

media = (soma / 5)
print(f"Valor da soma {soma}, Valor da media {media}")