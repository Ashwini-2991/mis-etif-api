from pymongo import MongoClient
from conf.app_config import Config

class MongodbConnector:
    
    def __init__(self):
      pass
    
    def connect_etif_db(self):
        client = MongoClient(Config.MONGODB_URI)
        db = client[Config.MONGODB_DATABASE]
        collection = db[Config.MONGODB_TEMPLATE_COLLECTION]
        return collection