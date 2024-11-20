from flask import Flask
from models.heladeria import Heladeria, Producto, Helado


def create_app():
    app = Flask(__name__)

    # Registrar los controladores
    from controllers.heladeria_controller import heladeria_bp # type: ignore
    app.register_blueprint(heladeria_bp)

    return app
