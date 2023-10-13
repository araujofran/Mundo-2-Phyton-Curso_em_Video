
print ('SOMA ENTRE OS NÚMEROS ÍMPARES e multiplos de 3, VAMOS LÁ!!!')

s=0
cont=0
for c in range (0,500+1):
    if c %3==0 and c%2==1:
        cont +=1
        print(c, end= ",")
        s+=c

print('\n')
print ('A soma entre ambos deu {} e a quantidade de numero impares e multiplos de três são {}.'.format(s,cont))
print ('VAI!')