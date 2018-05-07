from flask import Blueprint
from flask_restplus import Api

from .apis.namespace1 import api as ns1

blueprint = Blueprint('api', __name__, url_prefix='/api/1')
api = Api(blueprint,
    title='My Title',
    version='1.0',
    description='A description',
    # All API metadatas
)

api.add_namespace(ns1)
