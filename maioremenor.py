#Qual é o maior valor? Qual é o menor valor?
a = int(input(" valor de a "))
b = int(input(" valor de b "))
c = int(input(" valor de c "))

maior = 0 
menor = 0 

if a < b and b > c and c > a:
  maior = b
  menor = a
elif a > b and b < c and c > a:
  maior = c 
  menor = b
elif a < b and b > c and c < a:
  maior = b
  menor = c
elif a > b and b > c and c < a:
  maior = a
  menor = c
elif a > b and b < c and c < a:
  maior = a
  menor = b
  
print(f"{maior}, {menor}")


