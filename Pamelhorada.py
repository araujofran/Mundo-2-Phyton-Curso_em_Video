pa= int (input('Digite o primeiro termo da PA: '))
raz = int (input ('Digite a razão da PA: '))
c=1

print('an = [ {} ->'.format(pa), end='')
while c<10:
    pa +=raz
    c+=1
    print(' {}'.format(pa), end=' ')
    print ( ' ->' if c<10 else ']', end=' ')
    
print ('\n')
pergunta= str (input ('Você quer mais termos? [S/N] ')).strip().upper()

while pergunta =='S'and pergunta!= 0:
   
    extra= int (input ('Quantos termos extras a mais você quer? '))
    cont=0
    total=c+extra
    while cont<extra:
        pa +=raz
        cont +=1
        print(' {}'.format(pa), end=' ')
        print ( ' ->' if c<=extra else ']',end =' ')
    pergunta= str (input ('Você quer mais termos? [S/N] ')).strip().upper()
    print ('O numero total de termos gerados foi {} '. format(total))
print (' FIM ')