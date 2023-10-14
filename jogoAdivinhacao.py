import random

computador = random.randint(0,2)

jogador = int (input(' TENTE ADIVINHAR UM NUMERO ENTRE 0 A 2! JOGUE: '))

palpites=1

while jogador != computador:
    print ('COMPUTADOR: {} '. format(computador))
    print ('VOCÊ: {} '. format(jogador))
    jogador = int (input(' ERROU!COMPUTADOR VENCEU! JOGUE NOVAMENTE: '))
    palpites +=1

print (' Você acertou com {} palpites.O numero escolhido pelo computador foi {} e você {}'.format (palpites,computador,jogador))