from injector import singleton
from processors.template_processor import TemplateProcessor
from handler.template_handler import TemplateHandler
from dbutils.mongodbconnector import MongodbConnector
from common.api_response import APIResponse

def config_dependencies(binder):
    binder.bind(TemplateProcessor, to=TemplateProcessor, scope=singleton)
    binder.bind(TemplateHandler, to=TemplateHandler, scope=singleton)
    binder.bind(MongodbConnector, to=MongodbConnector, scope=singleton)
    binder.bind(APIResponse, to=APIResponse, scope=singleton)