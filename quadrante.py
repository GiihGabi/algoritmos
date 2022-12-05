angulo = float(input(" digite aqui o angulo "))
quad = angulo % 360


if quad <= 90:
  print( "está no 1° quadrante ")
elif quad <= 180:
  print(" está no 2° quadrante ")
elif quad <= 270:
  print(" está no 3° quadrante ")
else:
  print(" está no 4° quadrante ")