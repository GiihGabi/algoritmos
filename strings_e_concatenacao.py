#Strings
teste = ("Unimar")
print(type(teste))

nome = input("informe seu nome: ")
print(type(nome))

idade = 18
print(type(idade))

#Concatenação
print("Olá " + "mundo! " + "Estudadando " + "Strings")
print("Olá " + nome + " Estudadando " + "Strings")
print("olá " + nome + ", você tem " + str(idade) + " anos")
print(f"Olá {nome}, você tem {idade} anos")

if "123" == 123:
  print("igual")
else:
  print("diferente")

if "123" != 123:
  print("diferente")
else:
  print("igual")


