def producto_mas_rentable(prod1: dict, prod2: dict, prod3: dict, prod4: dict) -> str:
    productos = [prod1, prod2, prod3, prod4]
    mas_rentable = max(productos, key=lambda x: x['rentabilidad'])
    return mas_rentable['nombre']

# Ejemplo de uso
prod1 = {"nombre": "Samurai de fresas", "rentabilidad": 4900}
prod2 = {"nombre": "Samurai de mandarinas", "rentabilidad": 2500}
prod3 = {"nombre": "Malteda chocoespacial", "rentabilidad": 11000}
prod4 = {"nombre": "Cupihelado", "rentabilidad": 3200}
print(producto_mas_rentable(prod1, prod2, prod3, prod4))  # Output: Malteda chocoespacial
