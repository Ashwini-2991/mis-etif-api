from injector import inject
from flask import request, Blueprint
from processors.template_processor import TemplateProcessor
from common.api_response import APIResponse

template_api = Blueprint("template_api", __name__)

@inject
@template_api.route('/create/template', methods=['POST'])
def create_template(processor: TemplateProcessor, api_response: APIResponse ):
    data = {}
    data["name"] = request.form['name']
    data["templateMetadata"] = request.form['templateMetadata']
    data["templateMappings"] = request.form['templateMappings']
    data["templateTableMappings"] = request.form['templateTableMappings']
    status_code = processor.create_template(data, request.files)
    return api_response.create_response(status_code)

@template_api.route('/templates', methods=['GET'])
def get_templates(processor: TemplateProcessor, api_response: APIResponse):
    status_code, templates  = processor.get_templates()
    return api_response.create_response(status_code, templates)

    

     
    