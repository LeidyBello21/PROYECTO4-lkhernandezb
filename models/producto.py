from abc import ABC, abstractmethod

class Producto(ABC):
    @abstractmethod
    def calcular_costo(self):
        pass

    @abstractmethod
    def calcular_rentabilidad(self):
        pass

    @abstractmethod
    def calcular_calorias(self):
        pass

class Helado(Producto):
    def __init__(self, nombre, precio, ingredientes):
        self.nombre = nombre
        self.precio_publico = precio  # 'precio' cambiado por 'precio_publico'
        self.ingredientes = ingredientes  # Lista de ingredientes (pueden ser objetos de tipo Base o Complemento)

    def calcular_costo(self):
        # Aquí puedes implementar la lógica para calcular el costo de producción
        return 2.0  # Ejemplo de costo

    def calcular_rentabilidad(self):
        # Lógica para calcular la rentabilidad
        return self.precio_publico - self.calcular_costo()

    def calcular_calorias(self):
        # Aquí puedes implementar la lógica para calcular las calorías
        return 150  # Ejemplo de calorías
