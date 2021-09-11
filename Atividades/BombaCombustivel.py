class BombaCombustível:
    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.quantidadeCombustivel = quantidadeCombustivel
    
    def abastecerPorValor(self):
        valor = float(input("Insira o valor a pagar: "))
        litros = valor/self.valorLitro
        print("Foi colocado no veiculo %.1f litros" %litros)
        self.quantidadeCombustivel = self.quantidadeCombustivel - litros

    def abastecerPorLitro(self):
        litros = float(input("Insira quantos litros voce quer colocar: "))
        self.valorLitro = self.valorLitro * litros
        print("Valor a ser pago = %.1f" %self.valorLitro)
        self.quantidadeCombustivel = self.quantidadeCombustivel - litros

    def alterarValor(self):
        novoValor = float(input("Insira o novo valor do litro do combustivel: "))
        self.valorLitro = novoValor
        return self.valorLitro

    def alterarCombustivel(self):
        novoCombustivel = str(input("Insira o novo tipo de combustivel: "))
        self.tipoCombustivel = novoCombustivel
        return self.tipoCombustivel

    def alterarQuantidadeCombustivel(self):
        novaQuantidade = float(input("Insira a nova quantidade de combustivel na bomba: "))
        self.quantidadeCombustivel = novaQuantidade
        return self.quantidadeCombustivel

    def getTipo(self):
        return self.tipoCombustivel
    def getQuantidade(self):
        return self.quantidadeCombustivel
    def getValor(self):
        return self.valorLitro