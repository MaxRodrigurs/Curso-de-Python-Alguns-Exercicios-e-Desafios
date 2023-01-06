import random

sort=random.randint(0,5)
res=input('Adivinhe em qual numero eu pensei:')
if res == sort:
    print('Parabéns, você acertou.')
else:
    print('Quase, eu pensei em {}'.format(sort))