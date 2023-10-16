#jogador escolhe par ou ímpar
# se o total for diferente do input do jogadorescolhe[P/I]
# Verificação se Total é P ou I
# criando a variavel EscolheJogadorParouImpar
import random
numjogador= 0
Escolhe = 'P'
if numjogador % 2 == 0:
    Verifica= 'P'
else:
    Verifica = 'I'
cont=-1
while Escolhe == Verifica:
    if Escolhe != Verifica:
        break
    cont +=1
    numcpu =random.randint(0,10)
    print (20*'~')
    numjogador= int (input('Diga o valor: '))
    Escolhe =str (input('PAR OU IMPAR? [P/I]: ')).strip().upper()
    Total = numcpu + numjogador
    
    print ('O valor do computador foi {} e o seu foi {} resultado é : {} .'.format (numcpu,numjogador,Total))
    if Total % 2 == 0:
        Verifica= 'P'
    else:
        Verifica = 'I'
    
    if Escolhe == Verifica:
        print ('Você ganhou!')
        
    else:
        print ('Você Perdeu!')
print (20*'-=')
print ('GAME OVER! Você venceu {} vezes. '. format(cont))


