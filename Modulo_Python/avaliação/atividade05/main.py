"""
Implemente uma função chamada calculadora que:Receba dois números e uma operação 
(adição, subtração, multiplicação ou divisão).Retorne o resultado da operação.
Trate divisões por zero e exiba uma mensagem apropriada.Salve o histórico dela em um json
"""
import json
def calculadora():
    num1 = float(input('Digite o primeiro número: '))
    num2 = float(input('Digite o segundo número: '))
    print(' "Adição"    "Subtração"    "Multiplicação"    "Divisão"')
    operacao = input('Qua operação deseja: ').lower()
    resultado = 0
    try:
        match operacao:
            case 'adição':
                print(f'A soma dos números é {num1 + num2}')
                resultado = num1 + num2
            case 'subtração':
                print(f'A Subtração dos números é {num1 - num2}')
                resultado = num1 - num2
            case 'multiplicação':
                print(f'A Multiplicação dos números é {num1 * num2}')
                resultado = num1 * num2
            case 'divisão':
                print(f'A Divisão dos números é {num1 / num2} e resto {num1 % num2}')
                resultado = num1 / num2
    except ZeroDivisionError:
        print('Não é possivel dividir por 0')
    
    with open('dados.json', 'w', encoding='utf8') as leitura:
        json.dump(resultado, leitura)

calculadora()