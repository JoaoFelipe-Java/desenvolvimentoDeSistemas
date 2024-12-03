arquivo = 'main.txt'

#leitura = open(arquivo,'w')
# leitura.close()

with open(arquivo, 'w+') as leitura:
    leitura.write('TOP\n')
    leitura.write('TOP\n')
    leitura.write('TOP')

with open(arquivo, 'r') as leitura:
    print(leitura.read())