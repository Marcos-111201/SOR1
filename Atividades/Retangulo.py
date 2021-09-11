# Criar uma classe que modele retângulos.
# 1. Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
# 2. Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
# 3. Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidas de 
# um cômodo. Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés 
# necessárias para o local.

class Retangulo:
    def __init__(self, ladoA, ladoB):
        self.l1 = ladoA
        self.l2 = ladoB

    def setBaseAzulejo(self):
        self.l1 = int(input("Insira o novo valor da base do azulejo: "))
    def setAlturaAzulejo(self):
        self.l2 = int(input("Insira o novo valor da altura do azulejo: "))

    def setBaseComodo(self):
        self.l1 = int(input("Insira o novo valor da base do comodo: "))
    def setAlturaComodo(self):
        self.l2 = int(input("Insira o novo valor da altura do comodo: "))

    def getBaseAzulejo(self):
        return self.l1
    def getAlturaAzulejo(self):
        return self.l2

    def getBaseComodo(self):
        return self.l1
    def getAlturaComodo(self):
        return self.l2

    def perimetro(self):
        P = 2*(self.l1) + 2*(self.l2)
        return P

    def area(self):
        A = self.l1 * self.l2
        return A
    