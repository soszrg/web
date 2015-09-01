#encoding=utf-8

import requests
import threading

class SpiderBase(threading.Thread):
    SessionBase = ''
    LockBase = ''
    UrlBase = ''
    
    def __init__(self, url=None, session=None, sesTrue=True, lockTrue=True):
        threading.Thread.__init__(self)
        
        if url != None:
            self.UrlBase = url
            
        if sesTrue:
            self.SessionBase = requests.session()
        
        if lockTrue:
            self.LockBase = threading.Lock()
        
        if session != None:
            self.__session = session
        
    
    def run(self):
        pass
    
    def GetData(self, url):
        pass