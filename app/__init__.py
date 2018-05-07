from flask import Flask
from config import Config

app = Flask(__name__)

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    from .apiv1 import blueprint as api1
    app.register_blueprint(api1)

    return app
