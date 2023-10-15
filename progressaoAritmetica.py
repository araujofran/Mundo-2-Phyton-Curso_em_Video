pa= int (input('Digite o primeiro termo da PA: '))
raz = int (input ('Digite a razão da PA: '))
c=1
print('an = [ {} ->'.format(pa), end='')
while c<10:
    pa +=raz
    c+=1
    print(' {}'.format(pa), end='')
    print ( ' ->' if c<10 else ']',end='')
print (' FIM ')