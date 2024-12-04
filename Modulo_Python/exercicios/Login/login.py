import json
def login_usuario():
    while True:
        login = input('Digite seu usuario: ')
        senha = input('Digite sua senha: ')

        with open('dados.json', 'r', encoding='utf8') as leitura:
            dados = json.load(leitura)
            c_email = dados['email']
            c_senha = dados['senha']
            c_nome = dados['nome']
            if c_email == login and c_senha == senha:
                print(f'Seja bem vindo!{c_nome}.')
                break
            else:
                print('Login ou usuario errado.')