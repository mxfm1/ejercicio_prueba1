import random

lista_productos = []

def menu():
    print('-----------------MENU PIEZA--------------')
    print()
    print('1. Grabar Pieza. ')      
    print('2. Buscar Pieza. ')      
    print('3. Imprimir Pieza. ')      
    print('0. Salir. ') 

def mostrar_producto():
    for producto in lista_productos:
        print(producto)

def busqueda_producto(pieza):
    for producto in lista_productos:
        if producto['idpieza'] == pieza:    
            return producto
    
while True:     
    menu()
    op = int(input('Ingresa la opcion adecuada: '))
    if op == 1:
        id_pieza = input('Ingresa el código de serie de la pieza. Formato "XXXXXX-XXX" ')
        while len(id_pieza) < 10:
            id_pieza = input('El codigo identificador debe ser de una longitud minima de 10 carácteres. ')
        nombre = input('Ingresa el nombre del producto. ')
        precio_producto = int(input('Ingresa el precio unitario del producto. '))
        while precio_producto <0:
            precio_producto = int(input('El precio debe ser superior a 0. '))
        producto = {'idpieza':id_pieza,'nombrepieza':nombre,'precio':precio_producto}
        lista_productos.append(producto)
        print(f'El producto: {nombre.upper()} fue añadido exitosamente. ')
    if op == 2:
        print('-------------MENU BÚSQUEDA---------------')
        print()
        mostrar_producto()
        pieza = input('Ingresa el numero de serie del producto a buscar. ')
        producto = busqueda_producto(pieza)
        if producto['precio'] >= 500:
            nombre = producto['nombrepieza']
            id = producto['idpieza']
            precio = producto['precio']
            print(f'ID PRODUCTO: {id}')
            print(f'NOMBRE PRODUCTO: {nombre}')
            print(f'PRECIO PRODUCTO: {precio}')
        else:
            print('Producto sin stock. ')
    if op == 3:
        print('-------------REPORTE PIEZA-------------')
        print()
        mostrar_producto()
        pieza = input('Ingresa el numero de serie del producto a buscar. ')
        busqueda_producto(pieza)
        nombre = producto['nombrepieza']
        id = producto['idpieza']
        precio = producto['precio']
        print(f'ID PRODUCTO: {id}')
        print(f'NOMBRE PRODUCTO: {nombre}')
        print(f'PRECIO PRODUCTO: {precio}')
            
    if op == 0:
        print('Adios.')
        break