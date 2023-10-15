import math

x= int (input ('Digite um numero: '))

f = math.factorial (x)

print ('O resultado do fatorial de {}! ='.format(x), end='')

c = x

while c>0:
    print ( ' {} '.format(c), end='')
    print ('x' if c>1 else '=', end='')
    c-=1
print (' {}'.format(f))