productos ={
    'M001': ['Alimento Premium', 'comida', 'DogPlus', 10.0, True, False],
    'M002': ['Arena Aglomerante', 'higiene', 'CatClean', 8.0, False, False],
    'M003': ['Snack Dental', 'snack', 'BiteJoy', 1.0, True, True],
    'M004': ['Shampoo Suave', 'higiene', 'PetCare', 0.5, False, True],
    'M005': ['Correa Nylon', 'accesorio', 'WalkPro', 0.3, True, False],
    'M006': ['Cama Mediana', 'accesorio', 'CozyPet', 2.0, False, False] 
}


stock = {
    'M001': [32990, 12],
    'M002': [9990, 0],
    'M003': [5490, 25],
    'M004': [7990, 5],
    'M005': [11990, 7],
    'M006': [24990, 3]
}


def unidades_categoria(categoria):

    cat_buscada = categoria.lower().strip()
    total_unidades = 0 
    
    for codigo in productos:
        datos_producto = productos[codigo]
        categoria_producto = datos_producto[1].lower().strip()
        
        if categoria_producto == cat_buscada:
            if codigo in stock:
                unidades = stock[codigo][1]
                total_unidades = total_unidades + unidades
                
    print(f"El total de unidades disponibles es: {total_unidades}")

def busqueda_precio(p_min, p_max):
    resultados = []
    
    for codigo in stock:
        datos_stock = stock[codigo]
        precio = datos_stock[0]
        unidades = datos_stock[1] 
        
        if precio >= p_min and precio <= p_max and unidades > 0:
            if codigo in productos:
                nombre = productos[codigo][0] 
                texto_producto = f"{nombre}{codigo}"
                resultados.append(texto_producto)
                
    if len(resultados) > 0:
        resultados.sort() 
        print(f"Los productos encontrados son: {resultados}")
    else:
        print("No hay productos en ese rango de precios.")



def actualizar_precio(codigo, nuevo_precio):

    cod_buscado = codigo.upper().strip()
    codigo_real = None
    
    for key in stock:
        if key.upper() == cod_buscado:
            codigo_real = key
            
    if codigo_real is None:
        return False
        
    stock[codigo_real][0] = nuevo_precio 
    return True


def agregar_producto(codigo, nombre, categoria, marca, peso_kg, es_importado, es_para_cachorro, precio, unidades):
    cod_nuevo = codigo.upper().strip()
    
    for key in productos:
        if key.upper() == cod_nuevo:
            return False 

    return True

def eliminar_producto(codigo): 

    cod_buscado = codigo.upper().strip()
    codigo_real = None
    
    for key in productos:
        if key.upper() == cod_buscado:
            codigo_real = key
            
    if codigo_real is None:
        return False
    
    del productos[codigo_real]
    if codigo_real in stock:
        del stock[codigo_real]
    return True

def validar_codigo(codigo):
    if codigo.strip() == "":
        return False
    cod_nuevo = codigo.upper().strip()
    for key in productos:
        if key.upper() == cod_nuevo:
            return False
    return True

def validar_nombre(nombre):
    return nombre.strip() != ""

def validar_categoria(categoria):
    return categoria.strip() != ""

def validar_marca(marca):
    return marca.strip() != ""

def validar_peso_kg(peso_str):
    try:
        peso = float(peso_str)
        return peso > 0
    except ValueError:
        return False

def validar_es_importado(opcion_str):
    opcion = opcion_str.lower().strip()
    return opcion == "s" or opcion == "n"

def validar_es_para_cachorro(opcion_str):
    opcion = opcion_str.lower().strip()
    return opcion == "s" or opcion == "n"

def validar_precio(precio_str):
    try:
        precio = int(precio_str)
        return precio > 0
    except ValueError:
        return False

def validar_unidades(unidades_str):
    try:
        unidades = int(unidades_str)
        return unidades >= 0
    except ValueError:
        return False

def menu_principal():
    while True:
        print("\n========== MENÚ PRINCIPAL ==========")
        print("1. Unidades por categoría")
        print("2. Búsqueda de productos por rango de precio") 
        print("3. Actualizar precio de producto")
        print("4. Agregar producto") 
        print("5. Eliminar producto") 
        print("6. Salir") 
        print("=====================================") 

        opcion = input("Ingrese opción: ").strip()
        if opcion == "1":
            categoria = input("Ingrese categoría a consultar: ")
            unidades_categoria(categoria)
            
        elif opcion == "2":
            while True:
                try:
                    p_min = int(input("Ingrese precio mínimo: ")) 
                    p_max = int(input("Ingrese precio máximo: ")) 

                    busqueda_precio(p_min, p_max)
                    break 
                except ValueError:
                    print("Debe ingresar valores enteros")

        elif opcion == "3":
            while True:
                cod = input("Ingrese código del producto: ")
                nuevo_p_str = input("Ingrese nuevo precio: ") 
                
                if validar_precio(nuevo_p_str):
                    nuevo_p = int(nuevo_p_str)
                    exito = actualizar_precio(cod, nuevo_p)

                    if exito:
                        print("Precio actualizado")
                    else:
                        print("El código no existe")
                else:
                    print("Precio inválido. Debe ser un entero positivo.")
                
                repetir = input("¿Desea actualizar otro precio (s/n)?: ").lower().strip()
                if repetir != "s":
                    break 
                    
        elif opcion == "4":
            codigo = input("Ingrese código del producto: ")
            nombre = input("Ingrese nombre: ")
            categoria = input("Ingrese categoría: ")
            marca = input("Ingrese marca: ") 
            peso_str = input("Ingrese peso (kg): ")
            importado_str = input("¿Es importado? (s/n): ") 
            cachorro_str = input("¿Es para cachorro? (s/n): ")
            precio_str = input("Ingrese precio: ") 
            unidades_str = input("Ingrese unidades: ")
            
            if not validar_codigo(codigo):
                print("Error: Código no válido o ya existente.")
                continue
            if not validar_nombre(nombre):
                print("Error: El nombre no puede estar vacío.")
                continue
            if not validar_categoria(categoria):
                print("Error: La categoría no puede estar vacía.")
                continue
            if not validar_marca(marca):
                print("Error: La marca no puede estar vacía.")
                continue
            if not validar_peso_kg(peso_str):
                print("Error: El peso debe ser un número decimal mayor a cero.")
                continue
            if not validar_es_importado(importado_str):
                print("Error: Debe responder con 's' o 'n'.")
                continue
            if not validar_es_para_cachorro(cachorro_str):
                print("Error: Debe responder con 's' o 'n'.")
                continue
            if not validar_precio(precio_str):
                print("Error: El precio debe ser un número entero mayor a cero.")
                continue
            if not validar_unidades(unidades_str):
                print("Error: Las unidades deben ser un número entero mayor o igual a cero.")
                continue

            peso_kg = float(peso_str)
            es_importado = importado_str.lower().strip() == "s"
            es_para_cachorro = cachorro_str.lower().strip() == "s"
            precio = int(precio_str)
            unidades = int(unidades_str)
            
            resultado = agregar_producto(codigo, nombre, categoria, marca, peso_kg, es_importado, es_para_cachorro, precio, unidades)
            if resultado:
                print("Producto agregado")
            else:
                print("El código ya existe")
                
        elif opcion == "5":
            cod = input("Ingrese código del producto a eliminar: ")
            eliminado = eliminar_producto(cod)
            if eliminado:
                print("Producto eliminado")
            else:
                print("El código no existe")
                
        # --- Opción 6 ---
        elif opcion == "6":
            print("Programa finalizado.")
            break
            
        else:
            print("Debe seleccionar una opción válida")

if __name__ == "__main__":
    menu_principal()