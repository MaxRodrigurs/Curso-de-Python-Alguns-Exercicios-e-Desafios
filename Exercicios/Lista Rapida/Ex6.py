pedro=int(input('Quantos anos Pedro tem?'))
joana=int(input('Quantos anos Joana tem?'))
if pedro>joana:
    print('Pedro é mais velho que Joana por {}.'.format(pedro-joana))
elif joana>pedro:
    print('Joana é mais velha que Pedro por {} anos.'.format(joana-pedro))
else:
    print('Alguem ai digitou errado..')