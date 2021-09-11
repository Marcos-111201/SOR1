from Retangulo import *

b = int(input("Insira a base do azulejo do piso: "))
h = int(input("Insira a altura do azulejo do piso: "))

azulejo = Retangulo(b, h)

ladoA = int(input("Insira a medida da base do comodo: "))
ladoB = int(input("Insira a medida da altura da base do comodo: "))

comodo = Retangulo(ladoA, ladoB)

print("\n===================================================")
print("\t\t  INFORMACOES DO COMODO")
print("=====================================================")
print("Serão necessarios %d metros de rodape para o comodo" %comodo.perimetro())
print("A area do comodo = ", comodo.area())
print("Serao necessarios",comodo.area()/azulejo.area()," azulejos para preencher o comodo")
print("=====================================================")

comodo.setBaseComodo()
comodo.setAlturaComodo()

print("\n===================================================")
print("           INFORMACOES DO NOVO COMODO")
print("=====================================================")
print("Serão necessarios %d metros de rodape para o comodo" %comodo.perimetro())
print("A area do comodo = ", comodo.area())
print("Serao necessarios",comodo.area()/azulejo.area()," azulejos para preencher o comodo")
print("=====================================================")
