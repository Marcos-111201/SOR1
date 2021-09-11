#!/usr/bin/env python3

import json
import cgitb, cgi
cgitb.enable(display=0, logdir="./")

form = cgi.FieldStorage()

nome = form.getvalue('nome')
sobrenome = form.getvalue('sobrenome')
ano = form.getvalue('ano')
sexo = form.getvalue('sexo')
cpf = form.getvalue('cpf')
email = form.getvalue('email')
telefone = form.getvalue('fone')


print("Content-type:text/html\r\n\r\n")
print("""<center><h1 style= "background-color:grey">CONFIRMAÇÃO DOS DADOS</h1>""")
print("<br><br>") 
print("""<h3>""")
print("NOME:", nome)
print("<br><br>")
print("SOBRENOME:", sobrenome)
print("<br><br>")
print("DATA DE NASCIMENTO:", ano)
print("<br><br>")
print("SEXO:", sexo)
print("<br><br>")
print("CPF:", cpf)
print("<br><br>")
print("EMAIL:", email)
print("<br><br>")
print("Telefone:", telefone)
print("<br><br>")
print("<a href=../index.html>Voltar</a>")
print("""</h3></center>""")


dicionario = {
    "Pessoa": {
        "Nome": nome,
        "Sobrenome": sobrenome,
        "Ano": ano,
        "Sexo": sexo,
        "cpf": cpf,
        "Email": email,
        "Telefone": telefone
    }
}

cadastro = json.dumps(dicionario, indent=2)

with open ("confirmacao_cadastros.json", "a") as confirmacao_cadastros:
    confirmacao_cadastros.writelines(cadastro)

