import requests
from common.logger import logger

class RequestHandler:
    def __init__(self,base_url,token=None):
        self.base_url = base_url
        self.session = requests.Session()

        if token:
            self.session.headers.update({"Authorization": f"token {token}"})

    def get(self,path):
        res = self.session.get(f"{self.base_url.rstrip('/')}/{path.lstrip('/')}")
        logger.info("GET %s->%d",path,res.status_code )
        return res

        
    def post(self,path,body):
        res = self.session.post(f"{self.base_url.rstrip('/')}/{path.lstrip('/')}", json =body)
        logger.info("POST %s->%d", path, res.status_code)
        return res

        
    def put(self,path,body):
        res = self.session.put(f"{self.base_url.rstrip('/')}/{path.lstrip('/')}", json =body)
        logger.info("PUT %s->%d", path, res.status_code )
        return res


    def delete(self,path):
        res = self.session.delete(f"{self.base_url.rstrip('/')}/{path.lstrip('/')}")
        logger.info ("DELETE %s->%d", path,res.status_code)
        return res