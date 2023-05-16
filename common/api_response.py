from flask import make_response,  json

class APIResponse():
        
    def __init__(self):
      pass
  
    def create_response(self, code = 200, result=None, error=None):
        return make_response({"statuscode": code, "data":result, "error":error}, code)