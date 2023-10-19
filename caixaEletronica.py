num = int (input ('Qual o valor será sacado? R$ '))

resto= num % 50 
quantidadecedulas= int (num/50) 

resto3 =1

while resto3 !=0:
    
     print('O resto da conta  divido por R$50 é {} e a quantidade de cedulas é {} '.format (resto,quantidadecedulas))
     resto1= resto % 20 # ok
     quantidadecedulas= int(resto/20)

     print('O resto da conta  divido por R$20 é {} e a quantidade de cedulas é {} '.format (resto1,quantidadecedulas))

     resto2= resto1 % 10 # ok
     quantidadecedulas= int(resto1/10)  # OK

     print('O resto da conta  divido por R$10 é {} e a quantidade de cedulas é {} '.format (resto2,quantidadecedulas))
    
     resto3= resto2 % 1 # ok
     quantidadecedulas= int(resto2/1)
     print('O resto da conta  divido por R$1 é {} e a quantidade de cedulas é {} '.format (resto3,quantidadecedulas))

     print('Volte sempre!')
