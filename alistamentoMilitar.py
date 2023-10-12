from datetime import date

data_atual = date.today ().year

print('-=-'*35)

print ('O ano vigente atual é: {}.'.format(data_atual))

print('-=-'*35)

anoNascimento = int(input('Digite o ano do seu nascimento: '))

idade = (data_atual-anoNascimento)
quantoFalta = 18-idade

if idade <0:
    idade = idade*-1

print('-=-'*35)

print ('{} anos é sua idade atual.'.format(idade))

print('-=-'*35)

if idade <18:

    print(' Ainda não é hora de se Alistar, falta {} anos para o alistamento Militar.SE PREPARE!!! '.format(quantoFalta))

if idade ==18:

    print(' É Hora de se Alista para o serviço Militar se Prepare!!! ')
elif idade>18:
    print (' Tá velho - não precisa se Alistar soldado!!! ')

print('-=-'*35)

print ('\033[1;32;40mFora de forma! MARCHE!')

print('-=-'*35)