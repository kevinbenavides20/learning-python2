
'''
cree na funcionan que genere el lanzamiento de 2 dados (1-6) 
y que muestre por pantalla el mensaje ganador cuando genere un par de sei
 de lo contrario dira sigue intentando
'''

##importo mi biblioteca para generar numeros aleatorios enteros.
from random import randint

#generar o lanzar los valores de los 2 dados
def dices():
    dice1 = randint(1,6)
    dice2 = randint(1,6)
 
    return dice1, dice2

#salidas
d = dices()
d1 = d[0]
d2 = d[1]

print('Dices: ', d)
print('Dice 1:', d1)
print('Dice 2:', d2)

#print('DICE 1: ', dice1)
#print('DICE 2: ', dice2)