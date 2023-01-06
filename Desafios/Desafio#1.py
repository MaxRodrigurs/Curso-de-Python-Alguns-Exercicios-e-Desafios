import math

casa=float(input('Qual o valor da casa desejada?'))
sal=float(input('Qual a sua renda mensal?'))
anos=int(input('Em quantos anos pretende pagar a dívida?'))
prest=(sal*30)/100
parc=casa/anos
if parc<prest:
    print('Empréstimo aprovado, você tem que pagar {} reais durante {} anos para quitar a dívida de {}.'.format(parc, anos, casa ))
elif parc==prest:
    print('Empréstimo em ánalise...')
elif parc>prest:
    print('Empréstimo negado!')
print('Obrigado por consultar seu imóvel com a gente.')