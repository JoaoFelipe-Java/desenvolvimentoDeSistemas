
"""
Crie um class motorista e um class carro, associe o carro ao motorista e possibilite que ele acelere 
o carro e também acrescente algo ao porta malas
"""

class Motorista:
    def __init__(self, nome, carro):
        self.Nome = nome
        self.Carro = carro

class carro:
    def __init__(self, Modelo):
        self.modelo = Modelo
        self.acelerar_carro = 0
        self.malas = []
        
    def acelera_carro(self, velocidade):
        self.acelerar_carro += velocidade
    
    def adicionar_itens_malas(self, itens):
        self.malas = itens

nome_motorista = input('Digite seu nome: ')
carro_motorista = input('Digite a marca do carro: ')
velociade = int(input('Velocidade do carro: '))
quantidade_itens = int(input('Quantos itens vai adicionar ao porta malas? '))
itens_mala = []

for i in range(0, quantidade_itens):
    itens = input('O que vai colocar no porta malas: ')
    itens_mala.append(itens)

motorista = Motorista(nome_motorista, carro_motorista)
carro_motorista = carro(carro_motorista)
carro_motorista.acelera_carro(velociade)
carro_motorista.adicionar_itens_malas(itens_mala)

print(f'O nome do motorista é {motorista.Nome}, o modelo do carro é {motorista.Carro}')
print(f"Itens do porta mala: {carro_motorista.malas}")
print(f"A velocidade do carro é {carro_motorista.acelerar_carro}km")