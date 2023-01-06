import random

num=int(random.randint(0,10))
num1=int(random.randint(0,10))
if num==num1:
    print('Não existe números maiores ou menores, eles são iguais.\n{} e {}.'.format(num,num1))
elif num>num1:
    print('O primeiro número é maior que o segundo número.\n{} e {}.'.format(num,num1))
elif num1>num:
    print('O segundo número é maior que o primeiro número.\n{} e {}.'.format(num,num1))