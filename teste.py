
''' maior preço como vincular com nome???

produto = preço
string recebendo int

lista[menu]

'''
maior= 0
produto= ' '
item=' '
while True:

    produto = str(input('Produto: ')).strip()
    
    preco= float(input('Preço: '))
    if preco > maior:
       
        maior = preco
        item =produto

    resp =' '

    while resp not in 'SN':
        resp = str (input ('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print ( 'O produto {} é o maior preço R${:.2f} . ' .format(item,maior))

