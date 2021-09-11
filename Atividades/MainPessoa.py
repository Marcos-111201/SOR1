from Pessoa import *

nome = input("Insira o nome da pessoa: ")
idade = int(input("Insira a idade da pessoa: "))
peso = float(input("Insira o peso da pessoa: "))
altura = float(input("Insira a altura da pessoa: "))

pessoa = Pessoa(nome, idade, peso, altura)

pessoa.envelhecer()
pessoa.engordar()
pessoa.emagrecer()
pessoa.crescer()

print("\n==============================")
print("     CONSULTA NUTRICIONAL")
print("==============================")
print("Nome: %s" %pessoa.getNome())
print("Idade: %d anos"%pessoa.getIdade())
print("Peso:  %.1f kg"%pessoa.getPeso())
print("Altura: %.2f m" %pessoa.getAltura())
print("==============================")