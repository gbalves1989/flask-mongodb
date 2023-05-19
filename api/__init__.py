from flask_openapi3 import OpenAPI, APIBlueprint, Info
from flask_cors import CORS
from flask_pymongo import PyMongo


info = Info(
    title='Flask MongoDB API',
    version='1.0.0',
    termsOfService='http://example.com/terms/',
    contact={
        'name': 'API Support',
        'url': 'http://www.example.com/support',
        'email': 'support@example.com'
    },
    license={
        'name': 'Apache 2.0',
        'url': 'https://www.apache.org/licenses/LICENSE-2.0.html'
    }
)

app = OpenAPI(
    __name__,
    info=info,
    servers=[{'url': 'http://localhost:5000'}]
)
app.config.from_object('config')

CORS(app, origins=[
    'http://127.0.0.1:5000',
    'http://localhost:5000',
    'http://localhost:5000/api/v1',
    'http://localhost:5000/openapi'
])

mongodb_client = PyMongo(app)
db = mongodb_client.db

api = APIBlueprint('flask-mongodb', __name__, url_prefix='/api/v1')

from api.routes import course_route

app.register_api(api)
