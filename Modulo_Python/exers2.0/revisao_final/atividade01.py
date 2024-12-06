"""
Implemente um sistema de gerenciamento de estoque que inclua classes Produto, 
Estoque e métodos para adicionar, remover e verificar produtos. 
"""

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

class Estoque:
    def __init__(self):
        self.qnt_estoque = 0
        self.lista_produtos = []
    def att_estoque(self, estoque):
        self.estoque = estoque
    def remove_estoque():
        ...
    def add_estoque(self, produto):
        self.lista_produtos.append(produto)
        self.qnt_estoque += 1
    def show_estoque(self):
        for produto in self.lista_produtos:
            print(f'Nome : {produto.nome} / Preço : {produto.preco}')
        print(f'Quantidade : {self.qnt_estoque}')


while True:
    estoque = Estoque()
    lista_produtodos = []
    quantidade_produtos = int(input("Quantos produtos vai adicionar: "))

    for i in range(0, quantidade_produtos):
        produto_nome = input(f'Qual o nome do produro {i+1}: ')
        produto_preco = float(input(f'Qual o preço do {produto_nome} {i+1}: '))

        produto_objeto = Produto(produto_nome,produto_preco)

        estoque.add_estoque(produto_objeto)
    
    estoque.show_estoque()
    
    
