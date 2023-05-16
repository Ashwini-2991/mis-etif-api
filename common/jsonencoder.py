import json
from bson import ObjectId
from datetime import datetime

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        if isinstance(o, datetime):
            return o.isoformat()
        return json.JSONEncoder.default(self, o)
    
def custom_decoder(obj):
    if '__type__' in obj and obj['__type__'] == '__datetime__':
        return datetime.fromtimestamp(obj['epoch'])
    return obj

# Encoder function      
def custom_dumps(obj):
    return json.dumps(obj, cls=JSONEncoder)

# Decoder function
def custom_loads(obj):
    return json.loads(obj, object_hook=custom_decoder)