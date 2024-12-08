"""
Crie uma classe Pessoa com os atributos nome e idade. 
Adicione um método para retornar a data de nascimento.  
"""
from datetime import datetime

class Pessoa:
    def __init__(self, nome, idade):
        self.nome=nome
        self.idade=idade

nome = input('Digite seu nome: ')
idade = int(input('Digute sua idade: '))
pessoa1 = Pessoa(nome, idade)

data_atual = datetime.now().year
print(f'Oi {pessoa1.nome}, sua data de nascimento é {data_atual - pessoa1.idade}')
        