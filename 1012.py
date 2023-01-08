insert = input().split(' ')
A = float(insert[0])
B = float(insert[1])
C = float(insert[2])
PI = 3.14159

triangulo = A * C
circulo = PI * C * C
trapezio = (A + B)/2 * C
quadrado = B * B
retangulo = A * B

print(f"TRIANGULO: {triangulo:.3f}")
print(f"CIRCULO: {circulo:.3f}")
print(f"TRAPEZIO: {trapezio:.3f}")
print(f"QUADRADO: {quadrado:.3f}")
print(f"RETANGULO: {retangulo:.3f}")