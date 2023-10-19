print (25* '==')
print ('==============  BANCO GUANABARA  =================')
print (25* '==')

num = int (input ('Qual o valor será sacado? R$ '))

resto= num % 50 
quantidadecedulas= int (num/50) 

resto3 =1

while resto3 !=0:

     print (25* '==')
    
     print('Há {} cedula(s) de RS50,00. '.format (quantidadecedulas))
     resto1= resto % 20 # ok
     quantidadecedulas= int(resto/20)

     

     print('Há {} cedula(s) de RS20,00. '.format (quantidadecedulas))

     resto2= resto1 % 10 # ok
     quantidadecedulas= int(resto1/10)  # OK

     print('Há {} cedula(s) de RS10,00. '.format (quantidadecedulas))
    
     resto3= resto2 % 1 # ok
     quantidadecedulas= int(resto2/1)
     print('Há {} cedula(s) de RS1,00. '.format (quantidadecedulas))

     print (25* '==')

     print('Volte sempre!')
