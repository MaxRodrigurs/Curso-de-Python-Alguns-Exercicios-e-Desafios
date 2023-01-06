frase=str(input('Digite uma palavra:')).upper().strip()
print('Aparece {} vezes'.format(frase.count('A')))
print('A aparece primeiro na posição {}'.format(frase.find('A')+1))
print('A aparece por ultimo na posição {}'.format(frase.rfind('A')+1))