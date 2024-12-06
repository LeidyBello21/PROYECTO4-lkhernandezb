from flask import Flask, jsonify, request

app = Flask(__name__)

# Datos simulados para productos e ingredientes
productos = [
    {"id": 1, "nombre": "Helado de Vainilla", "calorias": 250, "rentabilidad": 3.5, "costo_produccion": 1.5},
    {"id": 2, "nombre": "Helado de Chocolate", "calorias": 300, "rentabilidad": 4.0, "costo_produccion": 2.0}
]

ingredientes = [
    {"id": 1, "nombre": "Vainilla", "es_sano": True},
    {"id": 2, "nombre": "Chocolate", "es_sano": False}
]

# Consultar todos los productos
@app.route('/api/productos', methods=['GET'])
def obtener_productos():
    return jsonify(productos)

# Consultar un producto por su ID
@app.route('/api/productos/<int:id>', methods=['GET'])
def obtener_producto_por_id(id):
    producto = next((p for p in productos if p['id'] == id), None)
    if producto:
        return jsonify(producto)
    return jsonify({"error": "Producto no encontrado"}), 404

# Consultar un producto por su nombre
@app.route('/api/productos/nombre/<nombre>', methods=['GET'])
def obtener_producto_por_nombre(nombre):
    producto = next((p for p in productos if p['nombre'].lower() == nombre.lower()), None)
    if producto:
        return jsonify(producto)
    return jsonify({"error": "Producto no encontrado"}), 404

# Consultar calorías de un producto por su ID
@app.route('/api/productos/<int:id>/calorias', methods=['GET'])
def obtener_calorias_producto(id):
    producto = next((p for p in productos if p['id'] == id), None)
    if producto:
        return jsonify({"calorias": producto['calorias']})
    return jsonify({"error": "Producto no encontrado"}), 404

# Consultar rentabilidad de un producto por su ID
@app.route('/api/productos/<int:id>/rentabilidad', methods=['GET'])
def obtener_rentabilidad_producto(id):
    producto = next((p for p in productos if p['id'] == id), None)
    if producto:
        return jsonify({"rentabilidad": producto['rentabilidad']})
    return jsonify({"error": "Producto no encontrado"}), 404

# Consultar costo de producción de un producto por su ID
@app.route('/api/productos/<int:id>/costo_produccion', methods=['GET'])
def obtener_costo_producto(id):
    producto = next((p for p in productos if p['id'] == id), None)
    if producto:
        return jsonify({"costo_produccion": producto['costo_produccion']})
    return jsonify({"error": "Producto no encontrado"}), 404

# Vender un producto según su ID
@app.route('/api/productos/<int:id>/vender', methods=['POST'])
def vender_producto(id):
    producto = next((p for p in productos if p['id'] == id), None)
    if producto:
        # Lógica para la venta, por ejemplo, disminuir inventario (simulada)
        return jsonify({"mensaje": f"Producto {producto['nombre']} vendido exitosamente."})
    return jsonify({"error": "Producto no encontrado"}), 404

# Consultar todos los ingredientes
@app.route('/api/ingredientes', methods=['GET'])
def obtener_ingredientes():
    return jsonify(ingredientes)

# Consultar un ingrediente por su ID
@app.route('/api/ingredientes/<int:id>', methods=['GET'])
def obtener_ingrediente_por_id(id):
    ingrediente = next((i for i in ingredientes if i['id'] == id), None)
    if ingrediente:
        return jsonify(ingrediente)
    return jsonify({"error": "Ingrediente no encontrado"}), 404

# Consultar un ingrediente por su nombre
@app.route('/api/ingredientes/nombre/<nombre>', methods=['GET'])
def obtener_ingrediente_por_nombre(nombre):
    ingrediente = next((i for i in ingredientes if i['nombre'].lower() == nombre.lower()), None)
    if ingrediente:
        return jsonify(ingrediente)
    return jsonify({"error": "Ingrediente no encontrado"}), 404

# Consultar si un ingrediente es sano por su ID
@app.route('/api/ingredientes/<int:id>/sano', methods=['GET'])
def es_ingrediente_sano(id):
    ingrediente = next((i for i in ingredientes if i['id'] == id), None)
    if ingrediente:
        return jsonify({"es_sano": ingrediente['es_sano']})
    return jsonify({"error": "Ingrediente no encontrado"}), 404

# Reabastecer un producto por su ID (simulado)
@app.route('/api/productos/<int:id>/reabastecer', methods=['POST'])
def reabastecer_producto(id):
    producto = next((p for p in productos if p['id'] == id), None)
    if producto:
        # Lógica para reabastecer el producto (simulada)
        return jsonify({"mensaje": f"Producto {producto['nombre']} reabastecido exitosamente."})
    return jsonify({"error": "Producto no encontrado"}), 404

# Renovar el inventario de un producto por su ID
@app.route('/api/productos/<int:id>/renovar', methods=['POST'])
def renovar_inventario(id):
    producto = next((p for p in productos if p['id'] == id), None)
    if producto:
        # Lógica para renovar inventario (simulada)
        return jsonify({"mensaje": f"Inventario de {producto['nombre']} renovado exitosamente."})
    return jsonify({"error": "Producto no encontrado"}), 404

if __name__ == '__main__':
    app.run(debug=True)
