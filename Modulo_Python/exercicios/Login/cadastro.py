import json
def cadastro_usuario():
    dados_usuario = {}

    nome = input('Digite seu nome: ')
    email = input('Digite seu email: ')
    cpf = int(input('Digite seu CPF: '))
    while True:
        senha = input('Digite sua senha: ')
        senha_repetir = input('Digite sua senha novamente: ')
        if senha == senha_repetir:
            break
        else:
            print('Senha errada!')
    dados_usuario.update({ 'nome': nome ,'email': email , 'cpf': cpf ,'senha': senha })
    with open('dados.json', 'w', encoding='UTF8') as leitura:
        json.dump(
            dados_usuario,
            leitura
        )
