class Conta:
    def __init__(self, conta, titular, saldo, limite):
        print('Criando a conta...'.format(self))
        self.__conta = conta
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo de {} do titular {}".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor
    def sacar(self, valor):
        self.__saldo -= valor
