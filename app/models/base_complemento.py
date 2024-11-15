
from ingredientes import Ingrediente

class Base(Ingrediente):
    def __init__(self, nombre, precio, calorias, inventario, es_vegetariano, sabor):
        super().__init__(nombre, precio, calorias, inventario, es_vegetariano)
        self.sabor = sabor
    
    def abastecer(self):
        self.inventario += 5

    # Getters y setters para 'sabor'
    def get_sabor(self):
        return self.sabor
    
    def set_sabor(self, sabor):
        self.sabor = sabor

class Complemento(Ingrediente):
    def abastecer(self):
        self.inventario += 10

    def renovar_inventario(self):
        self.inventario = 0
