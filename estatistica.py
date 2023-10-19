print (43*'=')
print ('--------------LOJA SUPER BARATÃO----------------')
print (43*'=')


total= 0
while True:
    produto= str (input('Nome do Produto: ')).strip()
    preco= float (input('Preço: R$ '))
    total +=preco
         
    resp = ' '
    while resp not in 'SN':
        resp = str (input ('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
    
   

print (' O total da compra foi R${:.2f} '.format(total))
print ('--------------FIM DO PROGRAMA----------------')