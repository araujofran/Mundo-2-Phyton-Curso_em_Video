

print(20*'-=-')
somapares=0
for c in range (1,7):
    n=int (input(' Digite um número: '))
    if n%2==0:
        somapares+=n

print ('A soma dos números pares é {}.'.format(somapares))

