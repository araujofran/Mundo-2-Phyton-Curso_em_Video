''' 
[1]Ler o primeiro termo de uma pa 
[2]Ler a razão de uma pa
[3]Mostrar os 10 primeiros termos /// aqui limitou a pa (10 repetições)

razão de uma pa  / formúla

razão = a2-a1

'''
print ('\n')

print('A PA : ',end='')

for pa in range (0,30,2):
    print (pa,end=',',)

print ('\n')

print ( 'O primeiro termo dessa PA é ',end=' ')

for pa in range (0,1,2):
    print (pa,'.')
print ('\n')

print ( 'O dois primeiros termo dessa PA é ',end=' ')

cont=0

for pa in range (0,40,2):
    if cont<2:
        cont+=1
        
        print (pa,end='->')

print ('\n')

print ( 'Os dez primeiros termos dessa PA são: ',end=' ')
cont=0
for pa in range (0,40,2):
   
    if cont<10:
        cont+=1
        print (pa,end='->',)

print('\n')      
