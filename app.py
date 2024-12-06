from flask import Flask, render_template, request, redirect, url_for, flash, session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.models import Usuario, Ingrediente, Producto, Base
from werkzeug.security import check_password_hash
from config import Config

# Configurar la aplicación Flask
app = Flask(__name__)
app.config.from_object(Config)

# Configurar base de datos
engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
Session = sessionmaker(bind=engine)

# Crear las tablas antes de la primera solicitud
def crear_tablas():
    print("Creando tablas...")
    Base.metadata.create_all(engine)

crear_tablas()

@app.before_request
def before_request():
    print("Este es un request antes de cada solicitud.")

# Ruta de inicio (Login)
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        nombre_usuario = request.form['nombre_usuario']
        contrasena = request.form['contrasena']

        with Session() as session_db:
            usuario = session_db.query(Usuario).filter_by(nombre_usuario=nombre_usuario).first()

            if usuario and check_password_hash(usuario.contrasena, contrasena):
                session['user_id'] = usuario.id
                session['user_role'] = 'admin' if usuario.es_admin else 'empleado' if usuario.es_empleado else 'cliente'
                flash(f"Bienvenido, {usuario.nombre_usuario}!", 'success')
                return redirect(url_for('index'))
            else:
                flash('Usuario o contraseña incorrectos.', 'danger')

    return render_template('login.html')

# Ruta principal (Inicio después de login)
@app.route('/')
def index():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    with Session() as session_db:
        productos = session_db.query(Producto).all()

    return render_template('index.html', productos=productos)

# Ruta para agregar un nuevo ingrediente
@app.route('/agregar_ingrediente', methods=['POST'])
def agregar_ingrediente():
    if 'user_role' not in session or session['user_role'] not in ['admin', 'empleado']:
        flash("No tienes permisos para realizar esta acción.", 'danger')
        return redirect(url_for('index'))

    try:
        nombre = request.form['nombre']
        tipo = request.form['tipo']
        inventario = float(request.form['inventario'])

        nuevo_ingrediente = Ingrediente(nombre=nombre, tipo=tipo, inventario=inventario)

        with Session() as session_db:
            session_db.add(nuevo_ingrediente)
            session_db.commit()
            flash("Ingrediente agregado exitosamente.", 'success')
    except Exception as e:
        flash(f"Error al agregar ingrediente: {e}", 'danger')

    return redirect(url_for('index'))

# Ruta para vender un producto
@app.route('/vender/<int:producto_id>', methods=['POST'])
def vender_producto(producto_id):
    if 'user_role' not in session or session['user_role'] == 'cliente':
        flash("No tienes permisos para realizar esta acción.", 'danger')
        return redirect(url_for('index'))

    try:
        with Session() as session_db:
            producto = session_db.query(Producto).get(producto_id)
            if producto and producto.ingrediente1:
                producto.ingrediente1.inventario -= 1
                session_db.commit()
                flash(f"Producto '{producto.nombre}' vendido.", 'success')
            else:
                flash("No se pudo vender el producto.", 'danger')
    except Exception as e:
        flash(f"Error al vender producto: {e}", 'danger')

    return redirect(url_for('index'))

# Ruta para consultar rentabilidad
@app.route('/rentabilidad/<int:producto_id>', methods=['GET'])
def consultar_rentabilidad(producto_id):
    if 'user_role' not in session or session['user_role'] != 'admin':
        flash("No tienes permisos para consultar la rentabilidad.", 'danger')
        return redirect(url_for('index'))

    with Session() as session_db:
        producto = session_db.query(Producto).get(producto_id)

    if producto:
        rentabilidad = producto.precio_publico * 0.2  # Ejemplo
        return f"Rentabilidad del producto {producto.nombre}: {rentabilidad}"
    else:
        flash("Producto no encontrado.", 'danger')
        return redirect(url_for('index'))

# Ruta para obtener productos
@app.route('/productos', methods=['GET'])
def get_productos():
    with Session() as session_db:
        productos = session_db.query(Producto).all()

    return render_template('productos.html', productos=productos)

# Ruta para cerrar sesión
@app.route('/logout')
def logout():
    session.clear()
    flash("Has cerrado sesión.", 'success')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
