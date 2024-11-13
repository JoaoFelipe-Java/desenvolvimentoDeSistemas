"""
2) João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar 
o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior 
que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve
pagar um multa de R$ 4,00 por quilo excedente. João precisa que você faça um 
fluxograma que leia a variável P (peso de peixes) e verifique se há excesso. 
Se houver, gravar na variável E (Excesso) e na variável M o valor da multa Que 
João deverá pagar. Caso contrário mostrar tais variáveis com o conteúdo ZERO.
"""
Peso_Peixe = float(input("Qual peso dos peixe: "))
Execesso = Peso_Peixe - 50
Valor_Multa = Execesso * 4

if Valor_Multa == 0:
    print("Dentro do exedente de quilos estipulado.")
else:
    print("Valor de quilos exedido, valor da multa",Valor_Multa)
