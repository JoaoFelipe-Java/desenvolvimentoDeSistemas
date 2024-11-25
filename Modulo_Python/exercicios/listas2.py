"""
a)  Crie um programa que solicite ao usuário que insira 4 números.
b)  Identifique e imprima o maior e o menor número da lista inserida.
"""
numeros = [] # cria uma lista vazia

#Add 4 numeros a lista 
for i in range(4):
    numero = int(input('Digite um numero: ')) #pede o dado para o usuario
    numeros.append(numero)# Add o dado na variavel "numeros"

print(numeros)
print('O maior numero é ',max(numeros))
print('O menor numero é ',min(numeros))