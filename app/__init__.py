from flask import Flask
from config import Config

app = Flask(__name__)

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    from .apis.apiv1 import blueprint as apiv1
    app.register_blueprint(apiv1)

    return app
