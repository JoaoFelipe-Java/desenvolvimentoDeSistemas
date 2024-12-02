from time import sleep as timer
import calendar
from datetime import datetime
import random 

def contador_de_segundos():
    segundos = int(input('Quantos segundos? '))

    for i in range(segundos, 0, -1):
        timer(i)
        print(f'{i} segundos')
    
    print('Acabou')
#tempo()

def calendario():
    ano = datetime.now().year
    dia = datetime.now().day
    mes = datetime.now().month

    print(f'Dia atual {dia}, mês atual {mes}')
    print(calendar.calendar(ano))
#calendario()

def sorteio():
    lista_alunos = ['Joao', 'Bruno', 'Lucas', 'Cecilia']
    soteado = random.choice(lista_alunos)
    print(soteado)
#sorteio()

def agenda_semanal():
    agenda = {}
    atividades = [
        "Ir à academia",
        "Trabalhar",
        "Aulas de inglês",
        "Almoço com amigos",
        "Estudar Python",
        "Caminhada no parque",
        "Sessão de filmes",
        "Jantar em família"
    ]

    dias_da_semana = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"]
    for dia in dias_da_semana:
        atividade_aleatoria = random.choice(atividades)
        agenda.update({dia:atividade_aleatoria})

    agenda_semanal = agenda

    for dia, atividade in agenda_semanal.items():
        print(f"{dia}: {atividade}")
#agenda_semanal()