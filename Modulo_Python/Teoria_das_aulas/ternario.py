#solução do Copilot
[print(f'8 x {i} = {8 * i}') for i in range(1, 11)]

# Minha solução
num = 8
tabuada = lambda numero, x: numero * x
for i in range (10):
    print(f'{num}x{i+1}={tabuada(num,i+1)}')

