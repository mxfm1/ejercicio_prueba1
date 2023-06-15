import random


fila = int(input("ingrese el numero de filas (entre 3 y 6)"))
while fila < 3 or fila > 6:
    fila = int(input('El numero debe ser comprendido entre 3 y 6 '))
columna = int(input("ingrese el numero de colummnas (entre 3 y 6)"))
while columna < 3 or columna > 6:
  columna = int(input('El numero debe ser comprendido entre 3 y 6. '))

matriz = []

for i in range(fila):
    fil = []
    for j in range(columna):
        num = random.randint(1,100)
        fil.append(num)
    matriz.append(fil)
    
print('Matriz resultante. ')
for fila in matriz:
    for elemento in fila:
        print(elemento,end=' ')
    print()