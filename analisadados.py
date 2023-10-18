print (43*'=')
print ('--------------CADASTRAMENTO----------------')
print (43*'=')
somaid=0
somahomem=0
somamulher19=0
while True:
    idade= int (input('Idade: '))
    if idade >18:
        somaid +=1
    sexo = ' '
    while sexo not in 'MF':
        sexo = str (input ('Sexo: ')).strip().upper()[0]
    if sexo =='F' and idade < 20:
        somamulher19 +=1
    elif sexo == 'M':
        somahomem +=1
        
    resp = ' '
    while resp not in 'SN':
        resp = str (input ('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break

print ('O número de pessoas cadastradas com mais de 18 anos: {}.'.format(somaid))
print ('O número de homens cadastrados: {}. '.format(somahomem))
print ('O número de mulheres com menos de 20 anos: {}. '.format(somamulher19))
print (' FIM')
