import random

arr = []

for _ in range(10):
    num_add = random.randint(1,100)
    arr.append(num_add)

try:
    num = int(input('Ingresa un numero. '))
    
    for numero in arr:
        if numero == num:
            print('El numero se encuentra en el array. ')
except ValueError:
    print('INGRESA NUMEROS AWEONAO. ')
               
print(arr)