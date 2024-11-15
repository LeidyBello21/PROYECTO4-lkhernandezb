def calcular_costo(ing1: dict, ing2: dict, ing3: dict) -> int:
    return ing1['precio'] + ing2['precio'] + ing3['precio']

# Ejemplo de uso
ing1 = {"nombre": "Helado de Fresa", "precio": 1200}
ing2 = {"nombre": "Chispas de chocolate", "precio": 500}
ing3 = {"nombre": "Mani Japonés", "precio": 900}
print(calcular_costo(ing1, ing2, ing3))  # Output: 2600
