from datetime import date

data_atual = date.today().year

anoNasc = int (input(' Ano nascimento: '))
idade = data_atual - anoNasc

if idade<0:
    idade= idade*-1

if idade < 9: 
    print ( 'MIRIM')
elif idade >=9 and idade<=14: 
    print ( 'INFANTIL')
elif idade >14 and idade <=19: 
    print ( 'JUNIOR')
elif idade >19 and idade<=20: 
    print ( 'SÊNIOR')
else:
    print ('MASTER')

print ('Sua idade é {} anos'.format(idade))