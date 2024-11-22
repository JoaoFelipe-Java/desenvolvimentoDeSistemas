#Escreva um algoritmo que calcule e imprima a tabuada do 8 (1 a 10)
numero = int(input('Digite um numero: '))

for i in range(1, 11):
    print(f'{numero}x{i}= {numero*i}')

#Faça um algoritmo que conte de 1 a 100 e a cada múltiplo de 10 emita uma mensagem: “Múltiplo de 10”.
for i in range(0,101):

    if i % 10 == 0:
        print(f'{i} é multiplo de 10')
    else:
        print(i)

#ler 3 números Depois de ler todos os números o algoritmo deve apresentar 
#na tela o maior dos números lidos

maior = 0

i = 0
while i < 3:
    i += 1
    numero = int(input(f'Digite o {i}º número: '))
    if numero > maior:
        maior = numero
print(f'O maior número é o : {maior}')