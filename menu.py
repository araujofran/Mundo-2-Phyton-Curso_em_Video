'''CALCULADORA'''
menu=0
a= float (input('Digite um número: '))
b= float (input('Digite um número: '))
while menu != 4:
    print (30* ('--'))
    print (' [0] SOMAR \n [1] MULTIPLICAR \n [2] MAIOR \n [3] NOVOS NÚMEROS \n [4] SAIR ')
    print (30* ('--')) 
    lista = (' SOMAR',' MULTIPLICAR ',' MAIOR','NOVOS NÚMEROS',' SAIR ')
    menu = int (input ('Qual a escolha? '))
    if menu == 0:
        resultado = a+b 
        print ('O resultado da soma deu {}.'.format(resultado))
    elif menu == 1:
         resultado = a*b
         print ('O resultado da multiplicação deu {}.'.format(resultado))
    elif menu == 2:
        if a>b:
            print (' O número {} é maior do que {}.'.format(a,b))
        else:
            print (' O número {} é menor do que {}.'.format(a,b))

    elif menu == 3:
        a= float (input('Digite um novo número: '))
        b= float (input('Digite um novo número: '))
   
print ('FIM')