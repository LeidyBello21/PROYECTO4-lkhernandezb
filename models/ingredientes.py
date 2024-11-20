from abc import ABC, abstractmethod

class Ingrediente:
    def __init__(self, nombre, precio, calorias, inventario):
        # Asegúrate de que el número de parámetros sea el correcto
        super().__init__(nombre, precio, calorias, inventario)

class Complemento(Ingrediente):
    def __init__(self, nombre, precio, calorias, inventario, es_vegetariano, es_extra):
        # Ajusta el número de parámetros para que coincida
        super().__init__(nombre, precio, calorias, inventario)
        self.es_vegetariano = es_vegetariano
        self.es_extra = es_extra


    def abastecer(self, cantidad):
        """Aumentar el inventario"""
        self.inventario += cantidad

    def reducir(self, cantidad):
        """Disminuir el inventario si hay suficiente"""
        if self.inventario >= cantidad:
            self.inventario -= cantidad
        else:
            raise ValueError(f"No hay suficiente inventario de {self.nombre}.")
