from app.models.base_complemento import Base,Complemento
from mejor_producto import producto_mas_rentable


class Heladeria:
    def __init__(self, productos, inventario_ingredientes):
        self.productos = productos  # Lista de productos disponibles (máx 4)
        self.inventario_ingredientes = inventario_ingredientes  # Lista de ingredientes
        self.ventas_dia = 0
    
    def producto_mas_rentable(self):
        return max(self.productos, key=lambda p: p.calcular_rentabilidad())

    def vender(self, nombre_producto):
        for producto in self.productos:
            if producto.nombre == nombre_producto:
                # Verificar ingredientes disponibles
                if self.verificar_ingredientes(producto.ingredientes):
                    self.reducir_inventario(producto.ingredientes)
                    self.ventas_dia += producto.precio_publico
                    return True
        return False
    
    def verificar_ingredientes(self, ingredientes):
        for ingrediente in ingredientes:
            if ingrediente['nombre'] in self.inventario_ingredientes:
                if isinstance(ingrediente, Base) and self.inventario_ingredientes[ingrediente['nombre']].inventario < 0.2:
                    return False
                elif isinstance(ingrediente, Complemento) and self.inventario_ingredientes[ingrediente['nombre']].inventario < 1:
                    return False
        return True

    def reducir_inventario(self, ingredientes):
        for ingrediente in ingredientes:
            if isinstance(ingrediente, Base):
                self.inventario_ingredientes[ingrediente['nombre']].inventario -= 0.2
            elif isinstance(ingrediente, Complemento):
                self.inventario_ingredientes[ingrediente['nombre']].inventario -= 1
