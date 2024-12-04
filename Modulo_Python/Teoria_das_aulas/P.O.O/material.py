class Cliente:
    def __init__(self, nome,idade):
        self.nome = nome
        self.idade = idade
        self.saldo = 0
        self.avaliacao = 4
    def adicionarSaldo(self,valor):
        self.saldo += valor
        print(f'O valor de {valor} foi adicionado.')
    def removerSaldo(self, valor):
        self.saldo -= valor
    def aviacao(self, avaliacao):
        avaliacao =int(input('Avalieomotorista >>'))
        self.avaliacao = avaliacao

cliente1 = Cliente('Victor',21)
cliente2 = Cliente('Leo',32)

cliente1.adicionarSaldo(100)
cliente1.removerSaldo(50)

cliente2.adicionarSaldo(50)
print(f'{cliente1.saldo} {cliente1.avaliacao}')