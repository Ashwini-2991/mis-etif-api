from injector import inject
from handler.template_handler import TemplateHandler
import os

class TemplateProcessor:
    @inject
    def __init__(self, handler: TemplateHandler):
        self.handler = handler
       
    def create_template(self, data, files):
      if 'file' not in files:
        return "Bad File"
      
      file = files['file']
      #guid = uuid.uuid4().hex
      #data['file_id'] = guid

      # # S3 connection details
      # S3_BUCKET = 'etif-hack2023-s3'
      # S3_PATH = 'templates'  # path to upload files

      # # Connect to S3 and upload files
      # s3 = boto3.client('s3')
      # s3.upload_fileobj(file, S3_BUCKET, S3_PATH + '/' + guid) 

      current_directory = os.getcwd()
      source_file_path = '/templates/'
      path = current_directory + source_file_path + file.filename
      file.save(path)
      return self.handler.create_template(data)
    
    def get_templates(self):
       return self.handler.get_templates()