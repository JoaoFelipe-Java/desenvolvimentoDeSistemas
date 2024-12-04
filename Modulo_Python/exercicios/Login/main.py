import json
from cadastro import cadastro_usuario as c_cadastro
from login import login_usuario as l_login

while True:
    try:
        opcao = int(input('Digite 1 para cadastrar e 2 para login: '))
        if opcao != 1 and opcao != 2:
            raise ValueError
        match opcao:
            case 1:
                c_cadastro()
                print('cadastrado')
            case 2:
                l_login()
                print('Login')
    except ValueError:
        print('Digite um valor valido')
    except Exception:
        print('Aconteceu um error!')