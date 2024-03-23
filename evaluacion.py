
def example():
    ans = 0
    operar = True

    while operar:
        try:
            numero = float(input('ingresar un numero'))
            ans += numero

            if numero == 0:
                operar = False
            else:
                print(ans)
        
        except ValueError:
            print('error')
    
    print(ans)

example()

'''
from random import randint
def play(y):
    return y +1


def do_it(x):
    return play(x * x)

def random_number():
    data = randint(0,100)
    return data, do_it(data)

ans = random_number()
print(f'value: {ans[0]}')
print(f'value: {ans[1]}')
'''