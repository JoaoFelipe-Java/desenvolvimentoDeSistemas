"""
Crie um jogo simples em Python:Um número secreto entre 1 e 100 é gerado aleatoriamente.
O jogador tem 5 tentativas para adivinhar o número.Após cada tentativa, o programa deve informar:

    "Muito alto!" se o palpite for maior que o número.
    "Muito baixo!" se o palpite for menor que o número.
    "Parabéns, você acertou!" se o palpite for igual ao número.

Caso o jogador não acerte após 5 tentativas, exiba "Game Over! O número era X".
Utilize a biblioteca random para gerar o número secreto.

"""
import random

while True:
    escolha_usuario = int(input('Escolha um numero de 1 a 100: '))
    numero_aleatorio = random.randint(0, 100)
    tentativas = 5
    print(numero_aleatorio)

    while tentativas > 0:
        print(f'Tentatiavs restantes: {tentativas}')
        escolha_usuario = int(input('Escolha um numero de 1 a 100: '))
        print
        if escolha_usuario > numero_aleatorio:
            print('"Muito alto!" seu palpite foi maior que o número.')
        elif escolha_usuario < numero_aleatorio:
            print('"Muito baixo!" seu  palpite foi menor que o número.')
        elif escolha_usuario == numero_aleatorio:
            print('"Parabéns, você acertou!" se o palpite foi igual ao número.')
        tentativas -= 1

    print(f'Game Over! O número era {numero_aleatorio}')
    break

        