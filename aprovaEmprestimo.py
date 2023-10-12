''' O valor da prestação mensal não pode exceder 30% valor do salário'''

salario = float (input ('Informe seu salário: R$ '))
emprestimo = float (input ('Emprestimo desejado: R$ '))
prazo = float (input ('Quantas prestações: '))

print (' O seu salário é de R$ {:.2f} , o emprestimo solicitado foi de R$ {:.2f},a quantidade de parcelas escolhida são {:.0f}.'. format(salario,emprestimo,prazo))

prestacaoMensal = emprestimo//prazo
margemAprovacao = salario*0.30
print (' A margem limite do seu emprestimo é de R$ {}.'.format(margemAprovacao))
valor = prestacaoMensal - margemAprovacao

if prestacaoMensal > margemAprovacao:
    print ('Emprestimo negado, porque excedeu em R$ {:.2f} o valor mensal permitido'.format (valor))
else:
    print('Aprovado!!! Parabéns!!! O Valor do das parcelas mensais ficaram em R$ {:.2f}'.format(prestacaoMensal))

print ('Obrigado!')


