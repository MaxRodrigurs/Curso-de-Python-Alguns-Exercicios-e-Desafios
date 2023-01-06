from time import sleep
cont=0
km=float(input('informe a distancia percorrida em km:'))
while cont!=1:
    band = int( input( '\ninforme a bandeira da corrida:' ) )
    if band==1 or band==2:
        if band == 1:
            res=km * 1.8
            print( 'Calculando...' )
            sleep( 2 )
            print( 'Valor total é {}.'.format( res ))
            cont=1
        elif band == 2:
                res = km * 2.3
                print( 'Calculando...' )
                sleep( 2 )
                print( 'Valor total é {}.'.format( res ))
                cont=1
    elif band!=1 or band!=2:
        print('Erro de bandeira..')
        sleep(2)
        print('Favor inserir a bandeira correta')
    else:
        print('Erro.')