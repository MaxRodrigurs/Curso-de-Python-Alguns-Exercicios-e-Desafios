import random
import math

ca = random.randint(1,100)
co = random.randint(1,280)
print('Seu cateto adjacente é {}, o cateto oposto é {} e logo sua hipotenusa será {:.2f}'.format(ca,co,(float(math.sqrt((ca**2)+(co**2))))))