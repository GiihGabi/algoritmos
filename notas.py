count = 0 

while(count < 5):
  aluno = input("nome do aluno: ")
  nota1 = float(input("nota 1: "))
  nota2 = float(input("nota 2: "))
  nota3 = float(input("nota 3: "))
  media = (nota1 + nota2 + nota3) / 3
  if media < 5:
    print(f"Reprovado, a media foi de: {media}")
  elif media >= 5 and media < 7:
    print(f"Exame")
  else:
    print(f"Aprovado, a media foi de: {media}")
  count = count + 1