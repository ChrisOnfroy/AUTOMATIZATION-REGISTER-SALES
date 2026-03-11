def registerventas():
    is_true = True

    while is_true :
        
        ventas = {}
        
        nombre_producto = input("Nombre del producto: ")
        
        precio_unitario = int(input("Precio unitario: "))
        
        cantidad_vendida = int(input("Cantidad vendida: "))
        
        nueva_venta = int(input("""Desea ingresar otra venta?:
        1 = SI
        2 = NO 
        """))
        if nueva_venta == 2 :
            return False
        