
import cmath

print("Equação do segundo grau: ax^2 + bx + c ")
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

delta = b**2 - 4 * a * c

raiz_1 = (-b + cmath.sqrt(delta)) / (2.0 * a)
raiz_2 = (-b - cmath.sqrt(delta)) / (2.0 * a)

print(f"raiz 1 = {raiz_1}")
print(f"raiz 2 = {raiz_2}")
