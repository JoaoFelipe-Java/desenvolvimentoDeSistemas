"""
Crie duas classes:
1 Autor, com os atributos:  Nome, nacionalidade e livros
2 Livro, com os atributos: titulo, ano e autor
Depois, escreva um programa que:Crie um autor e dois livros associados a ele.
Imprima o nome do autor e a lista dos seus livros.

"""

class Autor:
    def __init__(self, nome, nacionalidade):
        self.nome = nome
        self.nacionalidade = nacionalidade
        self.livro = []
    def recebe_livros(self, livro):
        self.livro.append(livro)
    def mostra_livro(self):
        for i in self.livro:
            print(f'Publicou os seguintes livro: {i.titulo}, ano de {i.ano}')     

class Livro:
    def __init__(self, titulo, ano):
        self.titulo = titulo
        self.ano = ano

autor1 = Autor('Joao', 'brasileira')
livro1 = Livro('Matematica', 1998)
livro2 = Livro('Logica', 2004)
autor1.recebe_livros(livro1)
autor1.recebe_livros(livro2)

print(f'O autor {autor1.nome}, de nacionalidade {autor1.nacionalidade}.')
autor1.mostra_livro()