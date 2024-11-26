
def armazenar_contatos():
    contatos = {}
    
    while True:
        nome = input("Digite o nome do contato (ou 'finalizar' para encerrar): ")
        if nome.lower() == 'finalizar':
            break
        numero_telefone = input(f"Digite o número de telefone de {nome}: ")
        contatos[nome] = numero_telefone
        #contatos.update({nome : numero_telefone}) #Outra alternativa de armazenar os dados

    print("\nContatos cadastrados:")
    for nome, numero in contatos.items():
        print(f"Nome: {nome}, Número: {numero}")

armazenar_contatos()
