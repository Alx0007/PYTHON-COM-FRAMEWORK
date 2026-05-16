

class Data:
    def __init__(self, dia, mes, ano):
        self.dia =  dia
        self.mes  = mes 
        self.ano =  ano

    def __str__(self):
        print(f'{dia}/{mes}/{ano}')    

    def bissexto(self, ano):
        if (ano % 400 == 0 or ano % 4 == 0) or (ano % 100 == 0):
            print('ano bissexto...')
        else:
            print('Não é bissexto...')

    def data_valida(self, dia, mes):
    
        meses   =  [0,1,2,3,4,5,6,7,8,9,10,11,12]
        dias_meses = [0,list(range(0,31)),
                    list(range(1,29)),
                    list(range(1,31)),
                    list(range(1,30)),
                    list(range(1,31)),
                    list(range(1,30)),
                    list(range(1,31)),
                    list(range(1,31)),
                    list(range(1,30)),
                    list(range(1,31)),
                    list(range(1,30)),
                    list(range(1,31))
                    ]
        if mes in meses:
           i =  meses.index(mes)
        if dia in dias_meses[i]:
           print('data válida')
        else:
           print('Data invalida')

ano =  int(input('ano: '))
mes =  int(input('Digite o número do mês: '))
dia =  int(input('Digite o dia:  '))


data  =  Data(dia, mes, ano)
data.bissexto(ano)
data.data_valida(dia, mes)
data.__str__()
       