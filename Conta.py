class Conta:
    def __init__(self, conta, titular, saldo, limite):
        print('Criando a conta...'.format(self))
        self.conta = conta
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def extrato(self):
        print("Saldo de {} do titular {}".format(self.saldo, self.titular))

    def deposita(self, valor):
        print("Depositando...".format(self))
        self.saldo += valor
    def sacar(self, valor):
        print("Sacando o dinheiro...".format(self))
        self.saldo -= valor
