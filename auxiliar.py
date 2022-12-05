a = int(input(" valor de a "))
b = int(input(" valor de b "))
c = int(input(" valor de c "))

aux = 0

if a < b and b > c and c > a:
  aux = c
  c = b
  b = aux
elif a > b and b < c and c > a:
  aux = b
  b = a 
  a = aux
elif a < b and b > c and c < a:
  aux = c
  c = a
  a = aux
  aux = b
  b = c 
  c = aux
elif a > b and b > c and c < a:
  aux = c 
  c = a
  a = aux
elif a > b and b < c and c < a:
  aux = a 
  a = c 
  c = aux
  aux = b
  b = a 
  a = aux

print(f"{a},{b},{c}")
