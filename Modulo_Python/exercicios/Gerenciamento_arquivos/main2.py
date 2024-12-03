import json
arquivo = 'teste.txt'
usuario = {
    'nome' : 'Emilia',
    'idade' : 15,
    'cep' : '88888-88'
}

with open('dados.json', 'w', encoding='UTF8') as leitura:
    json.dump(
        usuario,
        leitura,
        indent= 3
    )