print (25*'-=')
print ('TABUADA COM UM FLAG')
print (25*'-=')

num= int (input ('Digite o número da Tabuada: '))
print (25*'-=') 
while num>0:
    if num <0:
        break
    cont =0
    while cont<10:
        r = cont * num
        cont+=1
        print ('{} x {} = {}'.format (num,cont,r))
    print (25*'-=') 
    num= int (input ('Digite o número da Tabuada: '))
    print (25*'-=') 

print ('FIM! GRAÇAS A DEUS EU CONSEGUI!!!')
print (25*'-=')
