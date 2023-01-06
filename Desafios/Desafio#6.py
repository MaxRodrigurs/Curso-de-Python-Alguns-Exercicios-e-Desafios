import random
a1=random.randint(0,20)
a2=random.randint(0,20)
a3=random.randint(0,20)
if a1<a2+a3 and a2<a1+a3 and a3<a1+a2:
    if a1==a2:
        if a2==a3:
            print('Todos os lados são iguais. Triangulo equilatero. {}, {} e {}.'.format(a1,a2,a3))
        elif a2!=a3:
            print('Apenas dois lados iguais. Triangulo Isoscéles. {}, {} e {}.'.format(a1,a2,a3))
    if a1!=a2:
        if a2!=a3:
            if a3!=a1:
                print('Todos os lados são diferentes.Triangulo Escaleno. {}, {} e {}.'.format(a1,a2,a3))
else:
    print('Não é possivel fazer um triângulo.')