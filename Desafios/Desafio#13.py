me=0
ma=0
for c in range(1, 6):
    i = float(input('Digite o seu peso:'.format(c)))
    if c == 1:
        ma=i
        me=i
    else:
        if i>ma:
            ma=i
        elif i<me:
            me=i
print('O menor valor foi {} e o maior valor foi {}.'.format(me,ma))