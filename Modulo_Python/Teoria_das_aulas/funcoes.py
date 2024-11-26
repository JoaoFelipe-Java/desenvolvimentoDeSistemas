valorTotal = 0

# parametro - recebe o argumento
def somarValor(valorProduto):
    global valorTotal
    # valorProduto = float(input('PRECO DO PRODUTO'))
    valorTotal += valorProduto

# argumento - valor entre parenteses
somarValor(30)
somarValor(5)
somarValor(47)

print(f'valor total é de R$: {valorTotal}')

def soma(x , y , z=None): # O argumento z é opcional e tem um valor padrão de None
    if z is not None:
        print(f'{x} , {y} , {z} / {x+y+z}')
    else:
        print('Z NÃO EXISTE!')

soma(4,8,10)
soma(y=3,z=1,x=4)
soma(7,2)

def somarMuitos(*numeros):
    global valorTotal
    
    for numero in numeros:
        valorTotal += numero
    print(numeros, valorTotal)

somarMuitos(1,2)
somarMuitos(250,901,412,321)
somarMuitos(410, 1203)
somarMuitos(190283912, 1315789)

print(sum([1,5,7,8,9]))