sexo = str(input('Qual o seu genero? [M/F] ')).strip().upper()[0]
m = 'masculino'.upper()
f = 'feminino'.upper()


while sexo not in 'MF':
         
      sexo = str(input('Dados Inválidos.Por favor qual o seu genero? [M/F] ')).strip().upper()[0]
if sexo == 'M':
      print ('O seu sexo é {}'.format (m))
elif sexo == 'F':
       print ('O seu sexo é {}'.format (f))

