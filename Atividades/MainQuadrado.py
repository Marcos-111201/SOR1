from Quadrado import *

lado = int(input("Insira o lado do quadrado1: "))
q1 = Quadrado(lado)

lado2 = int(input("Insira o lado do quadrado2: "))
q2 = Quadrado(lado2)

print("\nPerimetro do Quadrado1 = ", q1.perimetro())
print("Area do Quadrado1 = ", q1.area())

print("\nPerimetro do Quadrado2 = ", q2.perimetro())
print("Area do Quadrado2 = ", q2.area())