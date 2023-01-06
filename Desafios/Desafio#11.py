soma=0
for c in range(1,7):
    n=int(input('Digite um numero qualquer:'))
    if n%2 == 0:
        soma=soma+n
print('O valor da soma dos pares é {}.'.format(soma))