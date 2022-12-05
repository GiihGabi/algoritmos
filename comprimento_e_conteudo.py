#teste de strings comprimento e conteúdo
a = input("insira aqui o texto 1: ")
b = input("insira aqui o texto 2: ")
print(len(a))
print(len(b))
#comprimento
if len(a) == len(b):
  print("elas possuem o mesmo comprimento")
else:
  print("elas não possuem o mesmo comprimento")

#conteúdo
if a == b:
  print("elas possuem o mesmo conteúdo")
else:
  print("elas não possuem o mesmo conteúdo")