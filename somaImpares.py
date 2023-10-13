
print ('SOMA ENTRE OS NÚMEROS ÍMPARES e multiplos de 3, VAMOS LÁ!!!')

s=0
for c in range (0,500+1):
    if c %3==0 and c%2==1:
        print(c, end=",")
        s+=c

print('\n')
print ('A soma entre ambos deu {}'.format(s))
print ('VAI!')