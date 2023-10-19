while True:

    num = int (input ('Qual o valor será sacado? R$ '))
    num50 = int (num/50)
    resto1= num%50

    
    while resto !=0:
        print ('Total de {} cedulas de R$50 '.format(num50))
        
        if resto!=0:
            resto =resto%20
            num20= int (resto/20)
            print ('Total de {} cedulas de R$20 '.format(num20))
        if resto!=0:
            resto =num20%10
            num10= int (num20/20)
            print ('Total de {} cedulas de R$10 '.format(num10))
        if resto!=0:
            resto =num10%10
            num01= int (num10/20)
            print ('Total de {} cedulas de R$1 '.format(num01))
        else:
            break
    print ('Volte sempre!')
