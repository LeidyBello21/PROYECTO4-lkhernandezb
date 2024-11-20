from flask import Flask, render_template
from models.producto import Helado  # Asegúrate de importar la clase Helado correctamente
from models.heladeria import Heladeria

app = Flask(__name__)

# Inicializa algunos productos de ejemplo
ingredientes_base = [
    # Aquí deberías definir tus ingredientes de ejemplo si no los has definido aún.
    {"nombre": "Leche", "inventario": 10},
    {"nombre": "Azúcar", "inventario": 5},
]

productos = [
    Helado(nombre="Helado de Chocolate", precio= 5.500, ingredientes=ingredientes_base),
    Helado(nombre="Helado de Vainilla", precio= 4.500, ingredientes=ingredientes_base),
    Helado(nombre="Helado de Fresa", precio= 4.750, ingredientes=ingredientes_base),
    Helado(nombre="Malteada de Chocolate", precio= 6.000, ingredientes=ingredientes_base)
]

heladeria = Heladeria(productos, ingredientes_base)

@app.route('/')
def index():
    return render_template('index.html', productos=heladeria.productos)

@app.route('/vender/<nombre_producto>', methods=['POST'])
def vender_producto(nombre_producto):
    resultado = heladeria.vender(nombre_producto)
    return render_template('index.html', productos=heladeria.productos, mensaje=resultado)

if __name__ == '__main__':
    app.run(debug=True)
