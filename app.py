from flask import Flask
from flask_cors import CORS
from api import process_template
from flask_injector import FlaskInjector
from conf.dependencies import config_dependencies

def create_app():

    app = Flask(__name__)
    CORS(app)
    register_blueprints(app)
    configure_dependencies(app)
    return app

def register_blueprints(app):
    app.register_blueprint(process_template.template_api, url_prefix='/etif')

def configure_dependencies(app):
    FlaskInjector(app=app, modules=[config_dependencies])
