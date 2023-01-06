import random
a1=str(input('Digite o nome do primeiro aluno:'))
a2=str(input('Digite o nome do segundo aluno:'))
a3=str(input('Digite o nome do terceiro aluno:'))
a4=str(input('Digite o nome do quarto aluno:'))
ran=[a1,a2,a3,a4]
al=random.choice(ran)
print('O aluno escolhido foi {}.'.format(al))