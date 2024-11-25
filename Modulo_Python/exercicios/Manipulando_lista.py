"""
a)Crie uma lista com os números `[5, 8, 2, 9, 1]`.
b)Ordene a lista em ordem crescente e depois em ordem decrescente.
c)Adicione o número `7` ao final da lista e depois insira o número `3` na posição 2.
d)Substitua o valor na posição 1 por `10` e remova o valor `9` da lista.
e)Exclua os elementos da posição 2 até a posição 4 (inclusive).
"""
#Lista 
numeros = [5, 8 , 2 , 9 ,1]
print(numeros)

numeros.sort() #Função sort ordena uma lista em ordem crescente
print(numeros)

numeros.sort(reverse=True) #Usa a função '.sort' com parametro reverso
print(numeros)

numeros.append(7) # Add o número 7 na lista, sua posição será a ultima
print(numeros)

numeros.insert(1, 3)# Add 3 na lista, sua posição é a segunda, isso não apaga o valor da 2 posição joga ele para frente
print(numeros)

numeros[0] = 10# substitui o valor da primeira posição por 10
print(numeros)

# deletando alguns dados
del numeros[4]
del numeros[3]
del numeros[2]
print(numeros)