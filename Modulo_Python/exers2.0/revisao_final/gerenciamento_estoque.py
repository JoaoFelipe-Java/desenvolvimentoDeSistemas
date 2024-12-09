"""
Implemente um sistema de gerenciamento de estoque que inclua classes Produto, 
Estoque e métodos para adicionar, remover e verificar produtos. 
"""

class Produto:
    def __init__(self, codigo, nome, preco):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco

class Estoque:
    def __init__(self):
        self.produtos = {}

    def adicionar_produto(self, produto):
        self.produtos.update({produto.codigo: produto})
        #self.produtos[produto.codigo] = produto
        print(f"Produto {produto.nome} adicionado/atualizado com sucesso.\n")

    def remover_produto(self, codigo):
        if codigo in self.produtos:
            produto_removido = self.produtos.pop(codigo)
            print(f"Produto {produto_removido.nome} removido do estoque.")
        else:
            print("Produto não encontrado no estoque.")

    def listar_produtos(self):
        for produto in self.produtos.values():
            print(f'A chave do produto: "{produto.codigo}" o nome do produto: "{produto.nome}" o preço do produto: "{produto.preco}"')

estoque = Estoque()
for i in range(1, 3):
    codigo = input('\nDigite um codigo para o produto: ')
    nome = input('nome do produto: ')
    preco = input('Preço do produto: ')
    produto = Produto(codigo, nome, preco)
    estoque.adicionar_produto(produto)
    

estoque.listar_produtos()

estoque.remover_produto(codigo='1')

estoque.listar_produtos()
 