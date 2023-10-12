a = float (input (' Primeiro número: '))
b = float (input (' Segundo número: '))

print ('-=-'*15)

if a>b:
    print ('O valor {:.0f} é maior que {:.0f}'.format(a,b))
elif b>a:
    print ('O valor {:.0f} é maior que {:.0f}'.format(b,a))
else:
    print ('Os  numeros {:.0f} e {:.0f} são iguais! '.format(a,b))

print ('-=-'*15)