def list_numbers():
    i = 1
    while i <= 10:
        print(i)
        i += 1
    print('i:', 1)
#list_numbers()

def list_numbers2():

    i = 1 
    status = True

    while status: 
        if i == 11:
            break
        print(i)
        i += 1
    
    print('i:',i)


#list_numbers2()
    
def list_numbers3():

    i = 1 
    status = True

    while status: 
        
        print(i)
        i += 1
        if i >10:
            status = False
    print('i:',i)
#list_numbers3()
    
def list_numbers4():

    i = 1 
    status = False

    while not status: 
        
        print(i)
        i += 1
        if i >10:
            status = True
    print('i:',i)

list_numbers4()    
