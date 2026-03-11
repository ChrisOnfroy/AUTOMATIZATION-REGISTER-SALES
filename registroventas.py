def registerventas():
    is_true = True
    contador = 0
    ventas = {}
    while is_true :
        contador += 1 
        
        nombre_producto = input("Nombre del producto: ")
        precio_unitario = int(input("Precio unitario: "))
        cantidad_vendida = int(input("Cantidad vendida: "))

        ventas[contador] = [nombre_producto, precio_unitario, cantidad_vendida]
    
        nueva_venta = int(input("""Desea ingresar otra venta?:
        1 = SI
        2 = NO 
        """))
        if nueva_venta == 2 :
            print(ventas)
            return False
        