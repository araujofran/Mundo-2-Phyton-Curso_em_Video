''' Jokenpô Jogo

pedra = mão fechada 
papel = mão aberta 
tesoura = dois dedos 
computador random 

'''
import random
itens = ('PEDRA', 'TESOURA','PAPEL')
computador = random.randint(0,2)


print ('-=-'*10)

print ('----- Vamos jogar JOKENPÔ!!! -------')

print (' Veja as opões: \n [0] PEDRA \n [1] TESOURA \n [2] PAPEL')
print ('-=-'*15)
jogue = int (input('ESCOLHA\n \n JO\nKEN\nPÔ\n\n'))


print ('-=-'*15)

print (' O computador jogou: {}.'.format(itens[computador]))
print (' Você jogou: {}.'.format(itens[jogue]))

 
'''
[0] PEDRA 
[1] TESOURA 
[2] PAPEL
'''
print ('-=-'*15)

if computador == jogue:
    print('EMPATE')
elif computador==0 and jogue==1: # (pedra x tesoura)
    print( 'COMPUTADOR VENCE! ')
elif computador==0 and jogue==2: # (pedra x papel)
    print( 'VOCE GANHOU! ')
elif computador==1 and jogue==2: # (tesoura x papel)
    print( 'COMPUTADOR VENCE! ')
elif computador==1 and jogue==0: # (tesoura x pedra)
    print( 'VOCE GANHOU! ')

elif computador==2 and jogue==1: # (papel x tesoura)
    print( 'VOCE GANHOU ')
elif computador==2 and jogue==0: # (papel x pedra)
    print( 'COMPUTADOR VENCE! ')

print ('-=-'*15)

print ('Quer Jogar de Novo???')

print ('-=-'*15)


