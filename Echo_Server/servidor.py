#SERVIDOR
import socket
import json
from Emprestimo import *

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostbyname("localhost")
port = 9999

serversocket.bind((host, port))

serversocket.listen()
print("Iniciando Servidor...")

# aceitaçao da conexao do cliente ao servidor
while True:
    clientsocket, addr = serversocket.accept()
    print("Conectado a %s" %str(addr))

    # loop para o cliente solicitar quantas simulaçoes de emprestimo ele quiser
    while True:
        # O servidor recebe do usuario o valor codificado da opção desejada
        opcao = clientsocket.recv(1024)
        opcao = opcao.decode("ascii")

        # Caso a opçao inserida for 1, é executada as linhas do codigo abaixo
        # onde há a criaçao de um objeto emprestimo passando os valores inseri-
        # dos pelo cliente para os metodos da classe Emprestimo e depois os
        # resultados dos metodos sao enviados para o cliente onde serao printados
        if opcao == "1":
            dados = clientsocket.recv(1024)
            dados = json.loads(dados.decode("ascii"))

            VE = float(dados[0])
            m = int(dados[1])
            i = float(dados[2])

            e = Emprestimo(VE, m, i)

            VF = e.valorFinal()
            Parc = e.valorParcela(VF)
            JE = e.jurosEfetivo(VF)

            valores = [Parc, JE]
            valores = json.dumps(valores)
            clientsocket.send((valores.encode("ascii")))

        # Caso a opção inserida seja 2 é encerrada a conexao com o cliente
        elif opcao == "2":
            clientsocket.close()
            break