"""
LISTAS
"""
# metodos de uma lista
lista = ['Copo','Banana','KitKat','Bebida']
print(lista)

lista.append('VideoGame') # adicionar no final
print(lista)

lista.pop() # remover no final
print(lista)

lista.insert(2, 'tv') # inserir(indice, dado)
print(lista)

del lista[1] # deletar em um indice
print(lista)

# indice 0 1 2 3 4 / -5 -4 -3 -2 -1
print(lista[1]) # puxar por um indice

lista.remove('Bebida') # deletar pelo valor
print(lista)

lista.clear() # deletar tudo da lista
print(lista)

alunosPt1 = ['Carlos','Alessadra','Geraldo']
alunosPt2 = ['Guilherme','Paloma','Natan']

alunosPt3 = alunosPt1 + alunosPt2
print('Concatenando listas',alunosPt3)

alunosPt1.extend(alunosPt2)
print('Exentendo lista',alunosPt1)

# for + array
print(len(alunosPt1))

alunosPt1.append('Bruna')

for nome in alunosPt1:
    print(f'- {nome} \n ###')