import os

class RegistroProducto:
    def __init__(self):
        self.productos = {}

    def registrar_producto(self):
        # Solicita al usuario que ingrese los datos del producto
        id = int(input("Ingrese el ID del producto: "))
        nombre = input("Ingrese el nombre del producto: ")
        descripcion = input("Ingrese la descripción del producto: ")
        costo = float(input("Ingrese el costo del producto: "))
        cantidad = int(input("Ingrese la cantidad del producto: "))
        precio_venta = float(input("Ingrese el precio de venta: "))

        # Calcula el margen de venta basado en el costo y el precio de venta
        margen_de_venta = ((precio_venta - costo) / costo) * 100

        # Crea un diccionario para representar un producto
        producto = {
            'id': id,
            'nombre': nombre,
            'descripcion': descripcion,
            'costo': costo,
            'cantidad': cantidad,
            'precio_de_venta': precio_venta,
            'margen_de_venta': margen_de_venta
        }

        # Agrega el producto al diccionario 'productos' con 'id' como clave
        self.productos[id] = producto

    os.system('cls' if os.name == 'nt' else 'clear')
    def imprimir_productos(self):
        print("\nListado de productos:")
        for id, producto in self.productos.items():
            print(f"ID: {id}, Nombre: {producto['nombre']}, Descripción: {producto['descripcion']}, "
                  f"Costo: {producto['costo']}, Cantidad: {producto['cantidad']}, "
                  f"Margen de Venta (%): {producto['margen_de_venta']:.2f}%, Precio de Venta: ${producto['precio_de_venta']:.2f}")

# Creación de una instancia de la clase RegistroProducto
registro = RegistroProducto()

# Registro de productos a través de la consola
while True:
    registro.registrar_producto()
    continuar = input("\n¿Desea registrar otro producto? (s/n): ")
    if continuar.lower() != 's':
        break

# Llamada al método 'imprimir_productos' para mostrar los productos registrados
registro.imprimir_productos()

while True:
    repetir = input("\n¿Desea registrar otro producto? (s/n): ")
    if repetir.lower() == 's':
        registro.registrar_producto()
        registro.imprimir_productos()
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print ("Cerrando programa..... Hasta luego :D")
        break