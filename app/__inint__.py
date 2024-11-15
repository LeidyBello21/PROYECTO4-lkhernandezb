from flask import Flask


def create_app():
    app = Flask(__name__)

    # Registrar los controladores
    from .controllers.heladeria_controller import heladeria_bp
    app.register_blueprint(heladeria_bp)

    return app
