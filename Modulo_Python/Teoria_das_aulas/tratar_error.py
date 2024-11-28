#print(10 / 0) #ZeroDivisionError

lista = [0,1,2,3,4]
#print(lista[4]) #IndexError

dicionario = {'chave':'valor'}
#print(dicionario['valor']) #KeyError

try:
    num_1 = 15
    num_2 = 5
    num_3 = num_1 / num_2
    print(num_3)

    lista = [0,1,2,3,4]
    print(lista[3])
    
    raise Exception

except ZeroDivisionError as erro:
    print('Não pode dividir por zero: ',erro)
except IndexError as erro:
    print('Elemento não encontrado: ', erro)
except KeyError as erro:
    print('Chave não encontrada: ', erro)
except Exception:
    print('Error desconhecido: ',Exception)
finally:
    print('Execute o programa')

print('Passou')
