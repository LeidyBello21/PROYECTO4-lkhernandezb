from costos import calcular_costo

def calcular_rentabilidad(precio_venta: int, ing1: dict, ing2: dict, ing3: dict) -> int:
    costo = calcular_costo(ing1, ing2, ing3)
    return precio_venta - costo

# Ejemplo de uso
precio_venta = 7500
print(calcular_rentabilidad(precio_venta, ing1, ing2, ing3))  # Output: 4900
