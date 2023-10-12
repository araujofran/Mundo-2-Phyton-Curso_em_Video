a = float (input('Digite o valor do primeiro lado: '))
b= float (input('Digite o valor do segundo lado: '))
c= float (input ('Digite o valor do terceiro lado: '))

''' Condição de existencia são três Trues
a<b+c (True)
b<c+a (True)
c<a+b (True)

'''
if a<(b+c) and b<(c+a) and c<(a+b):

    print ('É um triângulo ! Os seu valores são {:.0f} , {:.0f} , {:.0f}'. format (a,b,c))
    if a==b and a==c and b==c:
        print ('Ele é um triângulo Equilátero')
    elif a==b and a!=c and c!=b:
        print ('Ele é um triângulo Isóceles')
    elif a!=b and a!=c and b!=c:
        print ('Ele é um triângulo Escaleno')

else:
    print ('Não é um triângulo')


