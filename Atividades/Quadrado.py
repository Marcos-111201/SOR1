class Quadrado:
    
    def __init__(self, lado):
        self.lado = lado

    def perimetro(self):
        p = self.lado * 4
        return p

    def area(self):
        a = self.lado * self.lado
        return a

    def getLado(self):
        return self.lado