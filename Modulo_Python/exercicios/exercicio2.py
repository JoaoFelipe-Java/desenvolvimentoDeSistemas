# Calcular idade de uma pessoa com a data de nascimento
from datetime import datetime # importando a função datetime para usar no codigo
DATA_NASCIMENTO = int(input("Qual a sua data de nascimento? ")) # Pedindo a idade do usuario
DATA_ATUAL = datetime.now() # pegando a data do sistema 
print("Sua idade é", DATA_ATUAL.year - DATA_NASCIMENTO) # Subtraí a data_user pela data atual e mostra a idade do usuario
