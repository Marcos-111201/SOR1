from Triangulo import *

lado1 = int(input("\nInsira o lado 1 do triangulo: "))
lado2 = int(input("Insira o lado 2 do triangulo: "))
base = int(input("Insira a base do triangulo:   "))
altura = int(input("Insira a altura do triangulo: "))

triangulo = Triangulo(lado1, lado2, base, altura)

opcao = 0
while opcao != 5:
    print("\n================================================")
    print("\t\t  MENU")
    print("================================================")
    print("[1]: Definiçao do Triangulo")
    print("[2]: Calcular Perimetro")
    print("[3]: Calcular Area")
    print("[4]: Calcular Hipotenusa")
    print("[5]: Sair do Programa")
    print("================================================")

    opcao = input("Insira a opçao: ")
    if opcao == '1':
        triangulo.definiçao()
    elif opcao == '2':
        print("\n### O perimetro do triangulo = ", triangulo.perimetro())
    elif opcao == '3':
        print("\n### A area do triangulo = ", triangulo.area())
    elif opcao == '4':
        print("\n### A hipotenusa do triangulo = ", triangulo.hipotenusa())
    elif opcao == '5':
        print("FIM DA EXECUÇÃO")
        break
    else:
        print("OPÇAO INVALIDA")
    
