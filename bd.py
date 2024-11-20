from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.modelos import Ingrediente, Producto, Base  # Asegúrate de que estas importaciones son correctas

app = Flask(__name__)

# Configura el motor de la base de datos
engine = create_engine('sqlite:///heladeria.db')

# Crea la sesión
Session = sessionmaker(bind=engine)

@app.route('/')
def index():
    # Inicia una nueva sesión con el contexto adecuado
    session = Session()

    # Agregar un nuevo ingrediente
    try:
        nuevo_ingrediente = Ingrediente(nombre="Chocolate", tipo="Sabor", inventario=20.0)
        session.add(nuevo_ingrediente)
        session.commit()
        print("Ingrediente agregado exitosamente.")
    except Exception as e:
        session.rollback()
        print(f"Ocurrió un error al agregar el ingrediente: {e}")

    # Verifica si los ingredientes fueron insertados correctamente
    ingredientes = session.query(Ingrediente).all()
    print("\nIngredientes en la base de datos:")
    for ing in ingredientes:
        print(f"ID: {ing.id}, Nombre: {ing.nombre}, Tipo: {ing.tipo}, Inventario: {ing.inventario}")

    # Agregar un producto si hay ingredientes disponibles
    try:
        ingrediente1 = session.query(Ingrediente).first()  # Asegúrate de que haya al menos un ingrediente
        if ingrediente1:
            nuevo_producto = Producto(
                nombre="Helado de Chocolate",
                precio_publico=5.000,
                calorias=200.0,
                ingrediente1_id=ingrediente1.id
            )
            session.add(nuevo_producto)
            session.commit()
            print("Producto agregado exitosamente.")
        else:
            print("No hay suficientes ingredientes para crear un producto.")
    except Exception as e:
        session.rollback()
        print(f"Ocurrió un error al agregar el producto: {e}")

    # Verifica los productos insertados
    productos = session.query(Producto).all()
    print("\nProductos en la base de datos:")
    for prod in productos:
        print(f"ID: {prod.id}, Nombre: {prod.nombre}, Precio: {prod.precio_publico}, Calorías: {prod.calorias}")
        if prod.ingrediente1:
            print(f"  Ingrediente 1: {prod.ingrediente1.nombre}")

    # Cierra la sesión al finalizar
    session.close()

    return "Flask App is Running!"

if __name__ == "__main__":
    app.run(debug=True)
