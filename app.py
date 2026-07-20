from flask import Flask

from config import Config

from database.database import db

from routes.auth import auth
from routes.admin import admin
from routes.justificativas import justificativas
from routes.api import api
from routes.ti import ti


def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    app.secret_key = Config.SECRET_KEY

    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(auth)

    app.register_blueprint(admin)

    app.register_blueprint(justificativas)

    app.register_blueprint(api)

    app.register_blueprint(ti)

    return app


app = create_app()


if __name__ == "__main__":
    app.run(debug=True)