def contar_calorias(ingredientes_calorias: list[int]) -> float:
    total_calorias = sum(ingredientes_calorias)
    return round(total_calorias * 0.95, 2)
