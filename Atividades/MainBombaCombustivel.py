from BombaCombustivel import *

tipo = "Etanol"
valor = 7
quant = 50

gasolina = BombaCombustível(tipo, valor, quant)

print("O tipo da gasolina é: ",gasolina.getTipo(),"\nCusta: ",gasolina.getValor(),"reais\nQuantidade de gasolina na bomba: ",gasolina.getQuantidade(),"litros")
print("==================================")
print("ABASTECER POR VALOR")
print("==================================")
gasolina.abastecerPorValor()
print("==================================")
print("ABASTECER POR LITRO")
print("==================================")
gasolina.abastecerPorLitro()
print("Restante de gasolina na bomba = ",gasolina.getQuantidade())
print("==================================")
gasolina.alterarCombustivel()
gasolina.alterarValor()
gasolina.alterarQuantidadeCombustivel()
print("==================================")
print("O tipo da gasolina é: ",gasolina.getTipo(), "\nCusta: ",gasolina.getValor(), "reais\nQuantidade de gasolina na bomba: ", gasolina.getQuantidade(), "litros")
print("==================================")
print("ABASTECER POR VALOR")
print("==================================")
gasolina.abastecerPorValor()
print("==================================")
print("ABASTECER POR LITRO")
print("==================================")
gasolina.abastecerPorLitro()
print("Restante de gasolina na bomba = ",gasolina.getQuantidade())
print("==================================")
