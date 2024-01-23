#Tipos de datos en Python
#Python es un lenguaje dinamicamente tipado
#Python es un lenguaje INTERPRETADO

#1. numericos
##Enteros Z
num1 = 42
print("num1:", type(num1))  
##Flotantes o decimales (reales) => float
num2 = 50.5
print("Num2: ", type(num2))
#Complejos => complex
num3 = 2j

#2. cadenas
my_name = "kevin"
my_lastname = "Benavides"
profile = '''
Kevin es uno de los mejores creadores de contenido'''
address = 'bario popular casa 308'
phone_number = "3006458943"
print("address", type(address))
print("profile", type(profile))

a = 1
b = 1
suma1 = a + b #suma aritmetica

c = 1
d = 301 
suma2 = c + d #suma cadenas (concatenacion)

suma3 = a + c
print('suma1', suma1)
print('suma2', suma2)
print('suma3', suma3)

#3. logicos (valores o expresiones boleanas)
usuario_activo = True
print('usuario_activo', type(usuario_activo))
pago_realizado = False
print('usuario_activo', type(usuario_activo))

#4. listas
frutas = ['apple', 'banana']
colors = ['blue','red','white','green','brown']
print(frutas)
print((frutas), type(frutas))
print(colors)

#5. tuplas
#6. diccionarios
#7. conjuntos