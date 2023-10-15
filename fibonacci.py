n = int (input ('Digite o número de termos que vc quer: '))

print (30*'~')
print ('FIBONACCI')
print (30*'~')

t1=0
t2=1
print (30*'~')
print ('{} -> {}'.format(t1,t2), end=' ')

c=3

while c<=n:
    t3=t1+t2
    c+=1
    t1=t2
    t2=t3
    print ('->{}'.format(t3), end=' ')

print( 'FIM')
