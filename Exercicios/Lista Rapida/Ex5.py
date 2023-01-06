tab=0
cont=0
num = int( input( 'Insira um valor para que possamos demonstrar a tabuada referente:\n' ) )
print('\tTabuada do {}\t\n'.format(num))
while cont!=7:
    print('\t---{}x{}={}---\t'.format(num,tab,(num*tab)))
    tab=tab+1
    cont=cont+1