"""
)Escreva um programa para um sistema de controle de estoque de uma loja. 
O programa deve:Usar um para armazenar os itens no estoque, onde as chaves são os nomes 
dos produtos e os valores são as quantidades disponíveis.Permitir que o usuário escolha uma das opções:

    Adicionar um novo produto ao estoque.
    Atualizar a quantidade de um produto existente.
    Verificar se um produto está disponível (quantidade maior que 0).
    Continuar exibindo o menu até que o usuário escolha sair.

"""
import os
clear = lambda: os.system('cls')
# Chave vai ser o nome, o valor a quantidade.
estoque = {
        'banana': 19,
        'cafe': 98,
        'agua': 0
        }

while True:
        
        print(' "Adicionar"    "Atualizar"    "Verificar"    "Sair"')
        escolha_usuario = input('Digite uma das opções: ').lower()
        match escolha_usuario:
            case 'adicionar':
                nome_produto = input('Digite o nome do produto: ')
                quatidade_produto = int(input('Digite a quantidade desse produto: '))
                estoque.update({nome_produto:quatidade_produto})
                print(estoque)
            case 'atualizar':
                escolha_produto = input('Digite o nome do produto para atualizar o estoque: ')
                if estoque.get(escolha_produto):
                    atualizar_estoque = input(f'Qual a quantidade atual de {escolha_produto}: ')
                    estoque[escolha_produto] = atualizar_estoque
                    print(estoque)
                else:
                    print('Produto não existe.')
                    print(estoque)
            case 'verificar':
                escolha_verificar = input('Qual produto deseja verificar estoque: ')
                print(estoque.get(escolha_verificar))
                if estoque.get(escolha_verificar):
                    if estoque[escolha_verificar] > 0:
                        print(f'A quatidade no estoque de {escolha_verificar} é {estoque[escolha_verificar]}')
                else:
                    print('Produto sem estoque')
            case 'sair':
                print
                break
        
        

