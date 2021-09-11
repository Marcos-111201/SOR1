# Classe Pessoa: Crie uma classe que modele uma pessoa:
# 1. Atributos: nome, idade, peso e altura
# 2. Métodos: Envelhecer, engordar, emagrecer, crescer. Obs: Por padrão, a cada ano que nossa pessoa envelhece,
# sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.

class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self):
        anos = int(input("Insira quantos anos a pessoa vai envelhecer: "))
        self.idade = self.idade + anos
        if self.idade < 21:
            self.altura = self.altura + (anos*0.05)
        return self.idade

    def engordar(self):
        massa = float(input("Insira quantos quilos a pessoa engordou: "))
        self.peso = self.peso + massa
        return self.peso
    
    def emagrecer(self):
        massa2 = float(input("Insira quantos quilos a pessoa emagreceu: "))
        self.peso = self.peso - massa2
        return self.peso

    def crescer(self):
        if self.idade >=21:
            centimetros = float(input("Insira quantos centimetros a pessoa cresceu: "))
            self.altura = self.altura + centimetros
        return self.altura

    def getNome(self):
        return self.nome
    def getIdade(self):
        return self.idade
    def getPeso(self):
        return self.peso
    def getAltura(self):
        return self.altura