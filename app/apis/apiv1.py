from flask import Blueprint
from flask_restplus import Api

from .resoures.cats import api as cats
from .resoures.video import api as video

blueprint = Blueprint('api', __name__, url_prefix='/api/1')
api = Api(blueprint,
    title='My Title',
    version='1.0',
    description='A description',
    # All API metadatas
)

api.add_namespace(cats)
api.add_namespace(video)
