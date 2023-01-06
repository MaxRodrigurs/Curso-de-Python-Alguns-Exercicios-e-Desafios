ano=int(input('Em que ano você nasceu?'))
fut=(2021-ano)
if fut<=9:
    print('Você tem {}. Categoria Mirim.'.format(fut))
elif fut>9 and fut<=14:
    print('Você tem {} anos. Categoria Infantil.'.format(fut))
elif fut>14 and fut<=19:
    print('Você tem {} anos. Categoria Junior.'.format(fut))
elif fut>19 and fut<=20:
    print('Você tem {} anos. Categoria Sênior.'.format(fut))
else:
    print('Muito tempo vívido. Categoria Master.')