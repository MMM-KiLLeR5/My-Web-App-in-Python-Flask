# main.py
from apispec.ext.marshmallow import MarshmallowPlugin
from flask import Flask
from flask_apispec.extension import FlaskApiSpec
from flask_cors import CORS
from apispec import APISpec
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'your_secret_key_here'
JWTManager(app)
CORS(app)

app.config.update({
    'APISPEC_SPEC': APISpec(
        title='Tele3Connection',
        version='v1',
        openapi_version='2.0',
        plugins=[MarshmallowPlugin()],
    ),
    'APISPEC_SWAGGER_URL': '/swagger/'
})
docs = FlaskApiSpec(app)
