class Triangulo:

    def __init__(self, lado1, lado2, base, altura):
        self.lado1 = lado1
        self.lado2 = lado2
        self.base = base
        self.altura = altura

    def perimetro(self):
        P = self.lado1 + self.lado2 + self.base
        return P

    def area(self):
        A = (self.base * self.altura)/2
        return A

    def hipotenusa(self):
        cateto1 = int(input("\nInsira o cateto oposto do triangulo: "))
        cateto2 = int(input("\nInsira o cateto adjascente do triangulo: "))
        H = (cateto1 **2 + cateto2 **2) **(1/2)
        return H

    def definiçao(self):
        if self.lado1 == (self.lado2 and self.base):
            print("\n### O triangulo é Equilatero")
        elif self.lado1 == self.lado2 and self.base != (self.lado1 and self.lado2):
            print("\n### O triagulo é Isosceles")
        else:
            print("\n### O triangulo é Escaleno")
