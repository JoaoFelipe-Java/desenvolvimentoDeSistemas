import json
import os 

class Aluno:
    def __init__(self, nome):
        self.nome = nome
        self.notas = []
    
    def adicionar_notas(self, nota):
        self.notas.append(nota)
    
    def calcular_media(self):
        if self.notas:
            return sum(self.notas) / len(self.notas)
        else:
            return 0
    
    def verifica_aprovacao(self):
        media = self.calcular_media()
        if media >= 7:
            print(f'Aluno(a) {self.nome} esta aprovado.')
        else:
            print(f'Aluno(a) {self.nome} esta reprovado.')
    
    def exportar_aluno(self):
        dados_aluno = {
            'nome': self.nome,
            'notas': self.notas,
            'media': self.calcular_media(),
            'aprovacao': self.verifica_aprovacao()
        }
        if os.path.exists('dados.json'):
            with open('dados.json', 'r', encoding='utf8') as leitura:
                try:
                    dados = json.load(leitura)
                except json.JSONDecodeError:
                    dados = []
                    print('Error, mas vai passar.')
        else:
            dados = []
        
        dados.append(dados_aluno)

        with open('dados.json', 'w', encoding='utf8') as leitura:
            json.dump(dados, leitura, indent=2)

aluno1 = Aluno('João')
aluno1.adicionar_notas(5)
aluno1.adicionar_notas(6)
aluno1.verifica_aprovacao()
aluno1.exportar_aluno()