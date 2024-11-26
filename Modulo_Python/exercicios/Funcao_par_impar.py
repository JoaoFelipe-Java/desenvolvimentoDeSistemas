"""
Crie uma função fala se um número é par ou ímpar. Retorne se o número é par ou ímpar.
"""
#numero = int(input('Digite um número: '))

def Par_impar(num):
    if num % 2 == 0:
        print(f'Esse numero é par: {num}')
    else:
        print(f'Esse número é impar: {num}')

#Par_impar(numero)

"""
 Crie uma função que multiplica todos os argumentos não nomeados recebidos e 
 Retorne o total para uma variável 
 e mostre o valor da variável.
 """
def operacao(*argumentos):
    resultado = 1

    for numero in argumentos:
        resultado *= numero
    print(f'O valor total da operação deu : {resultado}')

operacao(1,22,100)

"""
faça um algoritmo que leia três notas de um aluno, calcule e escreva a média 
final deste aluno. Considerar que a média é ponderada e que o peso das notas é 2,3 e 5.
"""
#Função para calcular a média ponderada
def calcular_media(nota1, nota2, nota3, peso1=2, peso2=3, peso3=5):
    soma_pesos = peso1 + peso2 + peso3
    media = (nota1 * peso1 + nota2 * peso2 + nota3 * peso3) / soma_pesos
    return media

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media_final = calcular_media(nota1, nota2, nota3)

print(f"A média final ponderada do aluno é: {media_final:.2f}")
