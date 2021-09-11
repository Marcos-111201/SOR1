# Fazer um sistema (servidor) que faça simulação de empréstimos, com informações passadas
# pelo usuário (Valor do empréstimo, Meses, Taxa de Juros) através de um cliente.
# O sistema deve informar o valor da prestação e a taxa de juros efetiva

class Emprestimo:

    def __init__(self, valorEmprestimo, meses, taxaJuros):
        self.VE = valorEmprestimo
        self.meses = meses
        self.taxa = taxaJuros

    def valorFinal(self):
        VF = self.VE * (1+(self.taxa/100)) **self.meses
        return VF

    def valorParcela(self, VF):
        Parc = VF/self.meses
        return Parc

    def jurosEfetivo(self, VF):
        JE = ((VF/self.VE)-1)*100
        return JE