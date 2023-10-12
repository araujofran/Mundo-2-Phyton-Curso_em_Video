import math

nota1 = float (input (' Digite a primeira nota: '))
nota2 = float (input (' Digite a segunda nota: '))

print ('*'*35)

media =float(nota1+nota2)/2

print (media)

print ( ' A primeira nota foi {:.2f} jutamente com a segunda nota {:.2f} deram uma média de {:.2f}.'.format (nota1,nota2,media))

if media<5:
    print (' REPROVADO')

elif media>= 5 and media <7:
    print (' RECUPERAÇÃO')

elif media >= 7:
    print (' APROVADO')

print ('*'*35)
