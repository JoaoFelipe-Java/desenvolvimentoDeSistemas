"""
1. Cadastro de Produto
Você precisa criar um programa que armazene informações de um produto em um 
dicionário. As informações devem incluir nome, preço e quantidade em estoque. 
Depois, o programa deve exibir todas as informações do produto.
"""
produtos = {
    'nomes' : ['pastel', 'Leite'],
    'precos' : [7.99, 5.0],
    'quantidade' : [56, 10]
}

nome = input('Nome do produto: ')
produtos.get('nomes').append(nome)

preco = float(input('Preco produto: '))
produtos.get('precos').append(preco)

quantidade = int(input('Quantidade de produtos: '))
produtos.get('quantidade').append(quantidade)

for produto in produtos.values():
    print(f'{produto[0]}')
    print(f'{produto[1]}')
    print(f'{produto[2]}')
    
    