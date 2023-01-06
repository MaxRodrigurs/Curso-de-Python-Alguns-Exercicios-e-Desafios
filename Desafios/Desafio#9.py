t=0
for c in range(0,500):
    if c%2 == 1 and c%3==0:
        t = t + c
print('O resultado da soma dos números impares e multiplos de 3 é {}.'.format(t))
