class Producto:
    def __init__(self, nombre, precio):
        self._nombre = nombre
        self._precio = precio

    @property
    def nombre(self):
        return self._nombre

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, nuevo_precio):
        if nuevo_precio < 0:
            print("Error: El precio no puede ser negativo.")
        else:
            self._precio = nuevo_precio

    def mostrar_informacion(self):
        print(f"Producto: {self.nombre}, Precio: ${self.precio:.2f}")

# Crear instancia de Producto
producto1 = Producto("Laptop", 1500.00)

# Mostrar información del producto
producto1.mostrar_informacion()

# Intentar asignar un precio negativo
producto1.precio = -500

# Asignar un precio válido
producto1.precio = 1200.00

# Mostrar información del producto actualizada
producto1.mostrar_informacion()
