
from models.ingredientes import Ingrediente

class Base(Ingrediente):
    
    def __init__(self, nombre, precio, calorias, inventario, es_vegetariano, tipo):
        super().__init__(nombre, precio, inventario)  # Solo pasa los parámetros que necesita la clase padre
        self.calorias = calorias
        self.es_vegetariano = es_vegetariano
        self.tipo = tipo


    
    def abastecer(self, cantidad):
        self.inventario += cantidad  # Aumentamos el inventario

    def get_sabor(self):
        return self.sabor

    def set_sabor(self, sabor):
        self.sabor = sabor

class Complemento(Ingrediente):
    def __init__(self, nombre, precio, calorias, inventario, es_vegetariano, es_extra):
        super().__init__(nombre, precio, calorias, inventario, es_vegetariano)
        self.es_extra = es_extra

    def abastecer(self, cantidad):
        self.inventario += cantidad  # Aumentamos el inventario

    def renovar_inventario(self, cantidad):
        self.inventario = cantidad  # Establece el inventario a la cantidad especificada

    def es_extra_complemento(self):
        return self.es_extra
