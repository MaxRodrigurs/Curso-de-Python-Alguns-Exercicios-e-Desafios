ano=int(input('Em qual ano você nasceu ?'))
serv=(2021-ano)
if serv>18:
    res = serv - 18
    print('Já passou {} anos do tempo de se alistar.'.format(res))
elif serv<18:
    res=serv-18
    print('Você ainda tem {} até se alistar.'.format(res))
elif serv==18:
    print('Você tem que se alistar.')