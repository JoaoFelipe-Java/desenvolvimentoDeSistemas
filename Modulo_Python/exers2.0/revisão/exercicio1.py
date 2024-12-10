"""
1) faça uma calculadora com as 4 operações 
configuradas ( +,-,*,/)
"""

num1 = int(input('Digite o 1º número: '))
operador = input('Digite o operador')
num2 = int(input('Digite o 2º número: '))

match operador:
    case '+':
        resultado = num1 + num2
    case '-':
        resultado = num1 - num2
    case '*':
        resultado = num1 * num2
    case '/':
        resultado = num1 / num2
    case _:
        print('Digite um operador válido')

print(f'RESULTADO : {resultado}')
