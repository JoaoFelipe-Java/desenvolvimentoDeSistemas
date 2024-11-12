
# Algoritmo que leia nome, email e senha depois mostra na tela
NOME_PESSOA = str(input("Digite seu nome: "))
EMAIL_USER = str(input("Digite seu gmail: "))
SENHA_USER = int(input("Digite sua senha: "))

DADOS_USER = [NOME_PESSOA,EMAIL_USER,SENHA_USER]

print("Seu nome é ({}), seu gmail é ({}), sua senha é ({}).".format(DADOS_USER[0], DADOS_USER[1], DADOS_USER[-1]))