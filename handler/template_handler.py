import http.client
from injector import inject
from mongomock import ObjectId
from dbutils.mongodbconnector import MongodbConnector

class TemplateHandler():
    @inject
    def __init__(self, mongodbconnector: MongodbConnector):
        self.mongodbconnector = mongodbconnector

    def create_template(self, data):
        try:
            collection = self.mongodbconnector.connect_etif_db()
            collection.insert_one(data)
            return http.client.OK
        except:
            return http.client.INTERNAL_SERVER_ERROR
        
    
    def get_templates(self):  
        try:       
            collection = self.mongodbconnector.connect_etif_db()
            records = collection.find()

            templates = []

            for template in records:
                _id = template['_id']
                name = template['name']
                template_metadata = template['templateMetadata']
                captured_points = len(template['templateMappings'])
                captured_tables = len(template['templateTableMappings'])

                template = {
                    '_id' :  ObjectId(_id),
                    'name': name,
                    'templateMetadata' : template_metadata, 
                    'capturedPoints' : captured_points,
                    'capturedTables' : captured_tables
                }
                templates.append(template)    
            return http.client.OK, templates
        except:
            return http.client.INTERNAL_SERVER_ERROR
        
    def get_template_by_id(self, id):
        try: 
            collection = self.mongodbconnector.connect_etif_db()
            records = collection.find({_id : ObjectId(id)}) 

    

        
        