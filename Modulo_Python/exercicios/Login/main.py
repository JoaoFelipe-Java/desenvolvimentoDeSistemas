import json

# with open(arquivo1, 'w', encoding='UTF8') as leitura:
#     print()

#Deseja fazer "cadastro" ou "login":
while True:
    try:
        opcao = input('Deseja fazer "cadastro" ou "login":').lower()
        dados_usuario = {}
        if opcao == "cadastro":
            nome = input('Digite seu nome: ')
            email = input('Digite seu email: ')
            senha = input('Digite sua senha: ')
            senha_repetir = input('Digite sua senha: ')
            senha_final = []
            if senha == senha_repetir:
                senha_final = senha
            else:
                print('Senhas diferentes!')
                raise Exception
            dados_usuario.update({
                        'nome': nome,
                        'email': email,
                        'senha': senha_final
                     })
            with open('dados.json', 'w', encoding='UTF8') as leitura:
                json.dump(
                    dados_usuario,
                    leitura
                )
        else:
            print("Algo deu errado.")
            raise Exception
        break
    except Exception as error:
        print(error)
    except ValueError:
        print('Error de valor, execute novamente e digite "cadastro" ou "login" ')
