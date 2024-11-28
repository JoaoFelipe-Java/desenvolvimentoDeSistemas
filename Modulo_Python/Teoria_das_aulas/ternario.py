"""
Atividade01: Escreva um algoritmo que calcule e imprima a tabuada do 8 (1 a 10)
"""
[print(f'8 x {i} = {8 * i}') for i in range(1, 11)]# metodo 1

tabuada = [print(i * 8) for i in range(1,11)]
print(tabuada)

num = 8
tabuada = lambda numero, x: numero * x
for i in range (10):
    print(f'{num}x{i+1}={tabuada(num,i+1)}')

"""
Atividade02: Faça um algoritmo que avalie se o usuario e senha 
cadastrados e se não tiver, printe uma falha
senao printe que deu tudo certo
(considerar que usuario e senha sejam ''ADM')
"""
usuario = 'ADM'
senha = 'ADM'

valida_user = lambda user, senha: user == 'ADM' and senha == 'ADM'

print('Logado') if valida_user(usuario,senha) == True else print('erro')