usu=float(input('A quantos km você estava?'))
if usu>80:
    print('Você foi multado, você deve pagar {:.2f}.'.format((usu-80)*7))
else:
    print('Pode seguir viagem.')