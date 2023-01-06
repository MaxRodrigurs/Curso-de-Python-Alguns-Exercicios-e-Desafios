print('\t---------TABELA DE PROMOÇÕES---------\t\n---Álcool Até 25 litros, desconto de 2% por litro---\n---Acima de 25 litros, desconto de 4% por litro---\n---Gasolina Até 25 litros, desconto de 3% por litro---\n---Acima de 25 litros, desconto de 5% por litro---\t\n')
litro=float(input('Quantos litros você abasteceu:'))
tipo=str(input('Informe o tipo de cobustivel:\nAlcool-A    Gasolina-G\n')).upper()

if tipo=='A':
    if litro>=25:
        print('Valor total é {:.2f}.'.format((litro*1.9)*0.96))
    elif litro<25:
        print('Valor total é {:.2f}.'.format((litro * 1.9)*0.98))
elif tipo=='G':
    if litro >= 25:
        print('Valor total é {:.2f}.'.format((litro * 2.7)*0.95))
    elif litro < 25:
        print('Valor total é {:.2f}.'.format((litro * 2.7)*0.97))
else:
    print('Erro.')