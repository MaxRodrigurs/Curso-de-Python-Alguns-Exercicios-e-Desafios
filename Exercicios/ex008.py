import random
import math

met = random.randint(0,100)
print('Você tem {} metros, que refere-se a aproximadamente {} centimetros .'.format(met,math.ceil(met*100)))