"""
Crie uma classe Aluno que tenha os atributos nome, notas (uma lista) e 
métodos para calcular a média e verificar se o aluno foi aprovado (média >= 7). 
Todo aluno criado deverá ser adicionado a um Json
"""
import json

class Aluno:
    def __init__(self, nome):
        self.nome = nome 
        self.notas  = []
    
    def recebe_notas(self,nota):
        self.nota = nota
        self.notas.append(nota)

    def calcula_media(self):
        self.notas_somadas = sum(self.notas)
        self.media = self.notas_somadas / 4
        print(self.media)

nome = input('Digite teu nome: ')
aluno = Aluno(nome)
for i in range(0, 4):
    nota = float(input(f'Sua {i+1}ª nota:'))
    aluno.recebe_notas(nota)
aluno.calcula_media()
print(aluno.media)

dados_enviar = {
    aluno.nome : aluno.notas
}

with open("dados.json", 'r', encoding='utf8') as leitura:
    dados = json.load(leitura)
    dados_enviar.update(dados)
    print(dados_enviar)
    
with open("dados.json", 'w', encoding='utf8') as leitura:
    json.dump(
            dados_enviar,
            leitura,
            indent= 2
        )
    





