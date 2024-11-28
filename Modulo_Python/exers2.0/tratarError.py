"""
1)Peça ao usuário dois números e uma operação matemática (+, -, *, /). 
Execute a operação e trate erros como divisão por zero e operação inválida.
"""
def caculadora():
    try:

        num_1 = float(input("Digite primeiro número para calcular: "))
        num_2 = float(input("Digite segundo número para calcular: "))
        print('\nQual operação deseja efeutar?\nDigite 1 para Adição\nDigite 2 para subtração\nDigite 3 para multiplicação\nDigite 4 para divisão')
        operacao = int(input('Qual opção que deseja: '))

    except ValueError:
        #Caso o usuário digitar uma letra
        print("Error de valor, tente digitar um número.")
    
    try:
        match operacao:
            case 1:
                print(f'O resultado é: {num_1 + num_2}')
            case 2:
                print(f'O resultado é: {num_1 - num_2}')
            case 3:
                print(f'O resultado é: {num_1 * num_2}')
            case 4:
                print(f'O resultado é: {num_1 / num_2}')
    except ValueError:
        #Caso o usuário digitar uma letra
        print("Error de valor, tente digitar um número.")
    except UnboundLocalError:
        print('Execute o programa novamente!')
    except ZeroDivisionError:
        print('Impossivel dividir por zero')
        print('Execute o programa novamente!')

"""
Crie um dicionário com informações sobre um aluno (por exemplo, nome, idade, notas). 
Em seguida, solicite ao usuário uma chave para acessar no dicionário. 
Caso a chave não exista, trate o erro e informe quais chaves estão disponíveis.
"""
def aluno():
    try:
        alunos = {
            '232399': ['Joao','20 anos',[10,7,8,9,7]],
            '662233': ['Cecilia','20 anos',[10,7,8,9,7]],
            '111111': ['Bruno','20 anos',[10,7,8,9,7]]
        }
        chave = input("Digite a matricula do aluno: ").lower()
        print(alunos[chave])
    except KeyError:
        print("Essa chave não existe.")
        print('Execute o programa novamente!')

lista = [1,2,3,4,[10,11,12]]
print(lista[4][0])


