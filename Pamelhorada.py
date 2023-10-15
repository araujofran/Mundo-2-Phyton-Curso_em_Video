pa= int (input('Digite o primeiro termo da PA: '))
raz = int (input ('Digite a razão da PA: '))
c=1

print('an = [ {} ->'.format(pa), end='')
while c<10:
    pa +=raz
    c+=1
    print(' {}'.format(pa), end=' ')
    print ( ' ->' if c<10 else ']', end=' ')
print ('-> PAUSA')  
print ('\n')
pergunta= str (input ('Você quer mais termos? [S/N] ')).strip().upper()

while pergunta =='S':  
    extra= int (input ('Quantos termos extras a mais você quer? '))
    cont=0
    total=0
    while cont<extra:
        pa +=raz
        cont +=1
        print(' {}'.format(pa), end=' ')
        print ( ' ->' if c<extra else '->',end =' ')
        total=c+extra
    pergunta= str (input ('Você quer mais termos? [S/N] ')).strip().upper()

print ('O numero total de termos gerados foi {} '. format(total))
print (' FIM ')