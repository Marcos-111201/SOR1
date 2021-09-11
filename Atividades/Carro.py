# Classe carro: Implemente uma classe chamada Carro com as seguintes propriedades:
# - Um veículo tem um certo consumo de combustível (medidos em km / litro) e uma certa
# quantidade de combustível no tanque.
# - O consumo é especificado no construtor e o nível de combustível inicial é 0.
# - Forneça um método andar( ) que simule o ato de dirigir o veículo por uma certa
# distância, reduzindo o nível de combustível no tanque de gasolina.
# - Forneça um método obterGasolina( ), que retorna o nível atual de combustível.
# - Forneça um método adicionarGasolina( ), para abastecer o tanque.

class Carro:
    def __init__(self, consumo):
        self.consumo = consumo
        self.quantidade = 0

    def adicionarGasolina(self):
        gasolina = float(input("Insira a quantidade de gasolina a ser colocado:"))
        self.quantidade = gasolina
        return self.quantidade
    
    def obterGasolina(self):
        print("Quantidade atual de gasolina no tanque: %.1f litros" %self.quantidade)

    def andar(self):
        if self.quantidade == 0:
            print("O carro nao pode andar, sem gasolina")
        else:
            print("Ligando o carro")
            print("O carro esta andando...")
            distancia = float(input("Quantos quilometros o carro andou? "))
            self.quantidade = self.quantidade - (distancia*self.consumo)
        return self.quantidade

        