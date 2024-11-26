"""
2. Agenda de Contatos
Crie um programa para armazenar números de telefone. O usuário deve poder adicionar 
novos contatos (nome como chave e número como valor). Depois, o programa deve exibir 
todos os contatos cadastrados. Obs: O salvamento deverá parar apenas quando o 
usuário digitar "finalizar"
"""

agenda = {}

while True:
    nome = input('Digite o nome do usuario: ')
    if nome == 'final':
        break
    telefone = input(f'Digite telefone do {nome}: ')
    print('"""""""""""""""""""""""""')

    agenda.update({nome : telefone})

print('Contatos salvos')
for contato in agenda.items():
    print(f'\nNome: {contato[0]}')
    print(f'Telefone: {contato[1]}')

#print('\n',list(agenda.items()))
print(agenda)