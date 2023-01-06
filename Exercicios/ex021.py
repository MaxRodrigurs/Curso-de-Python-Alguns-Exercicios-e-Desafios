usu=float(input('Quantos km deseja viajar?'))
if usu<=200:
    print('Você deve pagar {}.'.format(usu*0.5))
else:
    print('Você deve pagar {}.'.format(usu*0.45))
print('Muito obrigado')