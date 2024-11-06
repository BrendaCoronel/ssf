def registrar_producto():
    """Función para registrar un nuevo producto."""

    def validar_precio(precio):
        """Valida que el precio sea un número positivo."""
        try:
            precio = float(precio)
            if precio <= 0:
                raise ValueError
            return precio
        except ValueError:
            print("El precio debe ser un número positivo.")
            return None

    def validar_cantidad(cantidad):
        """Valida que la cantidad sea un número entero positivo."""
        try:
            cantidad = int(cantidad)
            if cantidad < 0:
                raise ValueError
            return cantidad
        except ValueError:
            print("La cantidad debe ser un número entero positivo.")
            return None

    # Solicitar datos al usuario
    nombre = input("Ingrese el nombre del producto: ").strip()
    categoria = input("Ingrese la categoría del producto: ").strip()
    talla = input("Ingrese la talla del producto: ").strip()
    precio = input("Ingrese el precio del producto: ").strip()
    cantidad = input("Ingrese la cantidad en stock: ").strip()

    # Validar y convertir los datos
    precio_validado = validar_precio(precio)
    cantidad_validada = validar_cantidad(cantidad)

    if not nombre or not categoria or not talla or precio_validado is None or cantidad_validada is None:
        print("Error: Todos los campos deben ser completados correctamente.")
        return

    # Crear el producto en forma de diccionario
    producto = {
        "nombre": nombre,
        "categoria": categoria,
        "talla": talla,
        "precio": precio_validado,
        "cantidad": cantidad_validada
    }

    # Aquí es donde integrarías la lógica para almacenar el producto en la base de datos
    # Por ahora, simplemente mostramos el producto registrado
    print("Producto registrado con éxito:")
    for clave, valor in producto.items():
        print(f"{clave.capitalize()}: {valor}")

# Llamar a la función para probarla
registrar_producto()
