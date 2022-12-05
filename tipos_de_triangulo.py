A, B, C= input().split(" ")
A = float(A)
B = float(B)
C = float(C)
areaTRIANGULO = (A * C) / 2
areaareaCIRCULO = 3.14159 * (C ** 2)
areaTRAPEZIO = (A + B) / 2 * C
areaQUADRADO = (B * B)
areaRETANGULO = (A * B)
print(f"TRIANGULO: {areaTRIANGULO:.3f}")
print(f"CIRCULO: {areaareaCIRCULO:.3f}")
print(f"TRAPEZIO: {areaTRAPEZIO:.3f}")
print(f"QUADRADO: {areaQUADRADO:.3f}")
print(f"RETANGULO: {areaRETANGULO:.3f}")