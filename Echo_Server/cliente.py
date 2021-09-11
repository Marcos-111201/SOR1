#CLIENTE
import socket
import json

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "localhost"
port = 9999

s.connect((host, port))

# Descriçao para o usuario saber do que se trata o programa
print("\033[7:33: m##############################################\033[m")
print("\033[7:33: m             EMPRESTIMO BANCARIO              \033[m")
print("\033[7:33: m##############################################\033[m\n")
print("•Olá, seja bem vindo ao Simulador de Emprestimos;")
print("•Para simular um emprestimo insira:\n  -Valor do emprestimo\n  -Em quantos meses quer pagar\n  -Taxa de juros desejada")
print("•Voce recebera:\n  -O valor das parcelas a pagar a cada mes\n  -O valor da taxa de juros efetivos")
print("\033[4:37: mOBS: Os valores a serem inseridos nao podem ser inferioriores a 1\033[m")

opcao = 0
while opcao !=2:

    # Menu onde o usuario digitará o que ele deseja fazer: 1-enviar os valores
    # ou 2-finalizar a simulaçao
    print("\n\033[7:37: m      MENU: Escolha uma opção      \033[m")
    print("(1): ENVIAR DADOS")
    print("(2): FECHAR EXECUÇÂO")

    opcao = input("Insira a opcao: ")
    s.send(opcao.encode("ascii"))

    # Caso o usurario digite a opção 1 sera executado o programa pedindo para o usuario
    # inserir o valor do emprestimo, dos meses e da taxa de juros
    if opcao == "1":

        # Validaçao dos dados atraves do Try Except:
        while True:
            # Primeiro a clausula try é executada. Se nao ocorrer nenhuma excessao as linhas
            # abaixo sao executadas e apos isso quebra-se o loop e o programa segue adiante.
            try:
                print("\n============================================")
                VE = float(input("Insira o valor do emprestimo: "))

                meses = int(input("Insira em quantos meses voce quer pagar: "))

                taxa = float(input("Insira a taxa percentual desejada: "))
                print("============================================")
                break
            # Caso contrario(se ocorrer a excessao) o codigo entra no except e printa ao usu-
            # ário uma mensagem de erro
            except ValueError:
                print("\n\033[1:30:41m\t\t ERRO          \033[m")
                print("\033[1:31: mVALOR INVALIDO     \033[m")


        dados = [VE, meses, taxa]
        dados = json.dumps(dados)
        s.send(dados.encode("ascii"))

        valores = s.recv(1024)
        valores = json.loads(valores.decode("ascii"))

        Parcela = float(valores[0])
        JE = float(valores[1])

        # Exibiçao dos valores da Parcela e dos Juros Efetivos ao cliente
        print("\n=====================================")
        print("Valor da Parcela = %.4f" % Parcela)
        print("Taxa de Juros Efetivos = %.2f" % JE)
        print("=====================================")

    # Segunda opção do menu; Caso seja igual a 2 o cliente encerra sua conexao e
    # é mostrado ao usuario uma mensagem informando o fim da execuçao do programa
    elif opcao == "2":
        print("\n\033[7:35: m         FIM DA SIMULAÇAO          \033[m")
        s.close()
        break

    # Caso o usuario digite uma opçao diferente das acima(1 ou 2), sera
    # emitida uma mensagem de erro indormando-o para inserir uma opçao valida(1/2)
    else:
        print("\n\033[1:30:41m\t\t\t  ERRO              \033[m")
        print("\033[1:31: m\t    OPCAO INVALIDA      \033[m")
        print("\033[1:31: mINSIRA UMA OPÇAO VALIDA (1 ou 2)\033[m")