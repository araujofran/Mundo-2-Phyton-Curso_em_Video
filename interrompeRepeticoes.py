print (25* '~')

num= 0
cont=0
soma =0
while num!=999:
    num = int (input ('Digite um valor (999 para parar): '))
    if num==999:
        break
    cont +=1
    soma +=num
print (' A soma dos {} valores foi {} !'.format(cont,soma))
