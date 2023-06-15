import os


while True:
    print('---------------MENU PRINCIPAL--------------')
    print()
    print('1. Área de un circulo. ')
    print('2. Peimetro de un cuadrado. ')
    
    try:
        op = int(input('Ingresa una opcion. '))
        if op == 1:
            os.system('cls')
            print('CALCULAR EL AREA DE UN CIRCULO')
            x = int(input('Ingresa el radio del circulo. '))
            pi = 3.14
            area = pi * x**2
            print(f'El area del circulo seleccionado es {area} . ')
            break
        if op == 2:
            os.system('cls')
            print('CALCULO PERIMETRO SQR')
            lado = int(input('Ingresa el lado del cuadrado. '))
            perimetro = lado * 4
            print(f'El perimetro del cuadrado es {perimetro}')
            break
    except ValueError:
        print('Ingresa una opcion scw ')
           