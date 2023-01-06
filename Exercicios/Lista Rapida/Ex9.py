n1=float(input('Digite a 1 nota:'))
n2=float(input('Digite a 2 nota:'))
n3=float(input('Digite a 3 nota:'))
me=float(input('Digite a media dos exercicios:'))

res=(n1 + n2*2 + n3*3 + me)/7
if res>=9:
    print('Conceito A')
elif res>=7.5 and res<9:
    print( 'Conceito B' )
elif res >= 6 and res < 7.5:
    print( 'Conceito C' )
elif res >= 4 and res < 6:
    print( 'Conceito D' )
elif res<4:
    print( 'Conceito E' )
else:
    print('Erro.')