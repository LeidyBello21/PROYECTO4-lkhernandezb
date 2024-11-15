
from app.models.iproducto import IProducto

class Copa(IProducto):
    def __init__(self, nombre, precio_publico, tipo_vaso, ingredientes):
        self.nombre = nombre
        self.precio_publico = precio_publico
        self.tipo_vaso = tipo_vaso
        self.ingredientes = ingredientes

    def calcular_costo(self):
        return sum(ing['precio'] for ing in self.ingredientes)

    def calcular_calorias(self):
        calorias = sum(ing['calorias'] for ing in self.ingredientes)
        return round(calorias * 0.95, 2)

    def calcular_rentabilidad(self):
        return self.precio_publico - self.calcular_costo()

class Malteada(IProducto):
    def __init__(self, nombre, precio_publico, volumen, ingredientes):
        self.nombre = nombre
        self.precio_publico = precio_publico
        self.volumen = volumen
        self.ingredientes = ingredientes

    def calcular_costo(self):
        return sum(ing['precio'] for ing in self.ingredientes) + 500

    def calcular_calorias(self):
        calorias = sum(ing['calorias'] for ing in self.ingredientes)
        return calorias + 200

    def calcular_rentabilidad(self):
        return self.precio_publico - self.calcular_costo()
