class Data:
    def __init__(self, dia, mes, ano):
        print('Gerando data...'.format(self))
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def printData(self):
        print('{}/{}/{}'.format(self.dia, self.mes, self.ano))