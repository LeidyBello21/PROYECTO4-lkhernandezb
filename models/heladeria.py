from models.base_complemento import Base, Complemento

class Heladeria:
    def __init__(self, productos, inventario_ingredientes):
        self.productos = productos  # Lista de productos disponibles
        self.inventario_ingredientes = inventario_ingredientes  # Lista de ingredientes (Base y Complemento)
        self.ventas_dia = 0

    def get_ingrediente_por_nombre(self, nombre):
        """Obtiene un ingrediente por su nombre"""
        for ingrediente in self.inventario_ingredientes:
            if ingrediente.nombre == nombre:
                return ingrediente
        return None

    def producto_mas_rentable(self):
        """Devuelve el producto más rentable"""
        return max(self.productos, key=lambda p: p.calcular_rentabilidad())

    def vender(self, nombre_producto):
        """Realiza la venta de un producto si los ingredientes están disponibles"""
        try:
            for producto in self.productos:
                if producto.nombre == nombre_producto:
                    if self.verificar_ingredientes(producto.ingredientes):
                        self.reducir_inventario(producto.ingredientes)
                        self.ventas_dia += producto.precio_publico
                        return "¡Vendido!"
                    else:
                        for ingrediente in producto.ingredientes:
                            if not self.verificar_ingredientes([ingrediente]):
                                raise ValueError(ingrediente.nombre)
        except ValueError as e:
            return f"¡Oh no! Nos hemos quedado sin {e}"

    def verificar_ingredientes(self, ingredientes):
        """Verifica si los ingredientes están disponibles en el inventario"""
        for ingrediente in ingredientes:
            ingrediente_inventario = self.get_ingrediente_por_nombre(ingrediente.nombre)
            if ingrediente_inventario:
                if isinstance(ingrediente, Base) and ingrediente_inventario.inventario < 0.2:
                    return False
                elif isinstance(ingrediente, Complemento) and ingrediente_inventario.inventario < 1:
                    return False
            else:
                return False  # Si el ingrediente no se encuentra, retorna False
        return True

    def reducir_inventario(self, ingredientes):
     """Reduce el inventario de los ingredientes después de una venta"""
     for ingrediente in ingredientes:
        ingrediente_inventario = self.get_ingrediente_por_nombre(ingrediente.nombre)
        if ingrediente_inventario:
            if isinstance(ingrediente, Base):
                ingrediente_inventario.inventario -= 0.2  # Reducir el inventario de los ingredientes tipo Base
            elif isinstance(ingrediente, Complemento):
                ingrediente_inventario.inventario -= 1  # Reducir el inventario de los ingredientes tipo Complemento
