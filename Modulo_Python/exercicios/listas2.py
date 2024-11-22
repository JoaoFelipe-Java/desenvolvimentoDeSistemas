"""
a)  Crie um programa que solicite ao usuário que insira 4 números.
b)  Identifique e imprima o maior e o menor número da lista inserida.
"""
numeros = []
for i in range(4):
    numero = int(input('Digite um numero: '))
    numeros.append(numero)

print(numeros)
print('O maior numero é ',max(numeros))
print('O menor numero é ',min(numeros))