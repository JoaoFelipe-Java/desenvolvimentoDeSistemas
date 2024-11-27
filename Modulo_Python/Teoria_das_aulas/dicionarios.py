# DICIONARIO
# CHAVE E VALOR

usuario = {
    #chave : valor
    'nome' : 'Victor',
    'email' : 'emailtop@gmail.com',
    'senha' : '!123456',
    'cpf' : 99999999,
    'vip' : True,
    'endereco' : [
        {
            'rua' : '13',
            'cidade' : 'Ceilandia',
            'estado' : 'DF'
        }
    ]
}

print(usuario['nome'])
print(usuario, type(usuario))

# arquitetura de dic facilita o gerenciamento de dados 
# e a busca por eles (Obs: Até mesmo o crud)

# pesquisa = input('Digite o que quer achar:')
# print(usuario[pesquisa])

# METODOS PARA DICIONARIO
# len - QUANTAS CHAVES EXISTEM NO DICIONARIO
# keys - RETORNA AS CHAVES
# values - RETORNA OS VALORES
# items - RETORNA CHAVES E VALORES
# setdefault - ADICIONA VALOR SE A CHAVE NÃO EXISTE
# get - BUSCA CHAVE
# pop - APAGA UMA CHAVE ESPECÍFICA (del)
# popitem - APAGA A ULTIMA CHAVE
# update - ATUALIZA UM DICIONARIO
print(len(usuario))
print(list(usuario.keys()))
print(list(usuario.values()))
print(list(usuario.items()))

usuario.setdefault('saldo', 0)
print(usuario)

print(usuario.get('nome'))

usuario.pop('nome')
print(usuario)

usuario.popitem()
print(usuario)

usuario.update({
    'nome' : 'Victor',
    'email' : 'victor.rohod@docente.senai.br'
})
print(usuario)
