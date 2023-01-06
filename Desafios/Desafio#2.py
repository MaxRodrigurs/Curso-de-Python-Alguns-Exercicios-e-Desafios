import random
num=random.randint(0,100)
res=int(input('Qual base de conversão você deseja? \n1 para binário\t2 para octal\t3 para hexadecimal\n'))
if res==1:
    print('\nO número {} em binário fica {}.\n'.format(num,bin(num)))
elif res==2:
    print('\nO número {} em octal fica {}.\n'.format(num, oct(num)))
elif res==3:
    print('\nO número {} em hexadecimal fica {}.\n'.format(num,hex(num)))

print('Obrigado pela ajuda.')