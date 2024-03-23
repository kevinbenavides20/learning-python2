'''crar una calculadora que reciba 2 valores 
por consola y realice las operaciones aritmeticas basicas'''

import os
'''
os.system('clear')

#inputs
print("Ingrese primer valor: ")
n1 = int(input())

n2 = int(input("ingrese el segundo valor"))

suma = n1 + n2
print("suma: ", suma)

print(type(n1))
'''
os.system('clear')

def Todas(x, y):
    x + y
    x - y
    x * y
    x / y

def calculator(x, y, z):
   if z == '1' :
          return x + y
   elif z == '2':
      return x - y
   elif z == '3':
      return x * y
   elif z == '4':
      if y == 0:
          return 'No es posible dividir entre 0'
      else:
          return x / y
   elif z == '5':
        return x + y, x - y, x * y, x / y   
   else :
      print('::: Fail, invalid option :::')

n1 = float(input('ingrese primer valor: '))
n2 = float(input('ingrese segundo valor: '))

print('::: Menu calculadora :::')
print('[1]. Sumar')
print('[2]. Restar')
print('[3]. Multiplicar')
print('[4]. Dividir')
print('[5]. Todas')

opc = input('Digite una opcion del menu: ')

ans = calculator(n1, n2, opc)
print('resultado: ', ans)



