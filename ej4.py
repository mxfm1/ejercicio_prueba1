precio_total = 0
cantidad_cafe = 0
while True:
    print('---------------CAFETERIA--------------')
    print()
    print('ESPRESSO        $1500')
    print('CAPUCHINO       $1800')
    print('LATTE           $1600')
    print('MOCA            $1700')
    
    op = input('Ingresa el café que quieres llevar. ')
    if not op.isnumeric():
        print('Ingresa solo numeros. ')
    else:
        if op == 1:
            precio_total = precio_total + 1500
            cantidad_cafe = cantidad_cafe + 1
        if op == 2:
            pass
            cantidad_cafe += 1
        if op == 3:
            pass
            cantidad_cafe += 1
        if op == 4:
            pass
            cantidad_cafe += 1
        check = input(f'Usted lleva {cantidad_cafe} cafés y el total de la compra es {precio_total}. Quiere continuar?').upper()
        if check not in ['S','N']:
            continue 
        if precio_total > 3000:
            precio_total * 0.9
               
        print('--------COMPRA EXITOSA-------------')
        print()
        print(f'CANTIDAD CAFÉ:        {cantidad_cafe}') 
        print(f'TOTAL CAFE:           {total}') 