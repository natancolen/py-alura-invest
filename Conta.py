class Conta:
    def __init__(self, conta, titular, saldo, limite):
        print('Criando a conta...'.format(self))
        self.conta = conta
        self.titular = titular
        self.saldo = saldo
        self.limite = limite