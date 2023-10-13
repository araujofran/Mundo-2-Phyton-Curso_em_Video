print ('-=-'*20)
print ('TABUADA ONLINE')
print ('-=-'*20)

n2 = int(input('Digite o numero da tabuada:'))

for c in range (0,10+1):
        if c <=10:
            r=n2*c
            print('{} x {} = {}'.format(n2,c,r))
     
print ('-=-'*20)