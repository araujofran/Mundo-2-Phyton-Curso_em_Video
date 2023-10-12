from datetime import date

data_atual = date.today ().year



print ('O ano vigente atual é: {}.'.format(data_atual))
anoNascimento = int(input('Digite o ano do seu nascimento: '))

idade = (data_atual-anoNascimento)

print (' Sua idade atual é {} anos.'.format(idade))

if idade <18:

    print(' Ainda não é hora de se Alista para o serviço Militar se Prepare!!! ')

if idade ==18:

    print(' É Hora de se Alista para o serviço Militar se Prepare!!! ')
else:
    print (' Tá velho - não precisa se Alistar soldado!!! ')

print (' Fora de forma! MARCHE!')