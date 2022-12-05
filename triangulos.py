a = float(input(" medida do lado a "))
b = float(input(" medida do lado b "))
c = float(input(" medida do lado c "))


if a == b and b == c and c == a:
  print(" então será um triângulo equilátero ")
elif a == b or b == c or c == a:
  print(" então será um triângulo isósceles ")
elif a != b or b != c or c != a:
  print(" então será um triângulo escaleno ")