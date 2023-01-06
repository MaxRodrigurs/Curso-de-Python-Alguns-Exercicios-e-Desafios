import math
ang=float(input('Quantos angulos tem?'))
cos=math.cos(math.radians(ang))
sen=math.sin(math.radians(ang))
tan=math.tan(math.radians(ang))
print('Esse angulo tem {:.2f} de cosseno e {:.2f} de seno, {:.2f} de tangente'.format(cos, sen, tan))