from abc import ABC, abstractmethod

class Ingrediente(ABC):
    def __init__(self, nombre, precio, calorias, inventario, es_vegetariano):
        self.nombre = nombre
        self.precio = precio
        self.calorias = calorias
        self.inventario = inventario
        self.es_vegetariano = es_vegetariano
    
    def es_sano(self):
        return self.calorias < 100 or self.es_vegetariano

    @abstractmethod
    def abastecer(self):
        pass

# Getters y setters también pueden ser añadidos aquí.
