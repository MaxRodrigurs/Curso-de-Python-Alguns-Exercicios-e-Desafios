import random

num=str(random.randint(0,9999))
print('O valor escolhido foi {}'
      '\tUnidade: {}'
      '\tDezenas: {}'
      '\tCentenas: {}'
      '\tMilhar: {}'.format(num,(num[3]),(num[2]),(num[1]),(num[0])))
