''' Jokenpô Jogo

pedra = mão fechada 
papel = mão aberta 
tesoura = dois dedos 
computador random 

'''
import random
computador = random.randint(0,2)


print ('-=-'*10)

print ('----- Vamos jogar JOKENPÔ!!! -------')

print (' Veja as opões: \n [0] PEDRA \n [1] TESOURA \n [2] PAPEL')

jogue = int (input('Escolha \n JO\nKEN\nPÔ:'))


print (' O computador jogou: {}.'.format(computador))
print (' Você jogou: {}.'.format(jogue))
       
'''
[0] PEDRA 
[1] TESOURA 
[2] PAPEL
'''
if computador == jogue:
    print('EMPATE')
elif computador==0 and jogue==1: # (pedra x tesoura)
    print( 'Você perdeu, pedra ganha para tesoura! ')
elif computador==0 and jogue==2: # (pedra x papel)
    print( 'Você ganhou, pedra perde para papel! ')
elif computador==1 and jogue==2: # (tesoura x papel)
    print( 'Você perdeu, tesoura corta papel! ')
elif computador==1 and jogue==0: # (tesoura x pedra)
    print( 'Você ganhou, tesoura quebra na pedra! ')

elif computador==2 and jogue==1: # (papel x tesoura)
    print( 'Você ganhou, papel é cortado pela tesoura! ')
elif computador==2 and jogue==0: # (papel x pedra)
    print( 'Você perdeu, papel abraça a pedra! ')

print ('-=-'*15)

print ('Quer Jogar de Novo???')


