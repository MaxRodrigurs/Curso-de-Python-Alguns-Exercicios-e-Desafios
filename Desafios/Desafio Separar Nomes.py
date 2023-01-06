nome=str(input('Qual seu nome completo:')).strip()
no=nome.split()
print('Primeiro nome é: {}'.format(no[0]))
print('Ultimo nome é: {}.'.format(no[len(no)-1]))