# --*coding:utf-8*--
'''
Created on 2016年8月26日

@author: lwllovewf2010
'''
from llxx_client import llxx_client
from llxx_client import llxx_client_listner
import os

# pip install simplejson
import simplejson as json

class ServiceListner(llxx_client_listner):
    
    def __init__(self , target=None,
                 args=()):
        self._target = target
        
    def onMessage(self, message):
        #print ("receive message -> " + message)
        #target = json.JSONDecoder().decode(message)  
        #print target['action']  
        self._target(message)

def apk_service_listner(message):
        print ("apk_service receive message -> " + message)
        target = json.JSONDecoder().decode(message)  
        print target['action']  

def monkey_service_listner(message):
        print ("monkey_service receive message -> " + message)
        target = json.JSONDecoder().decode(message)  
        print target['action']  
 
if __name__ == '__main__':
    os.system("adb forward tcp:8082 tcp:8082")
    apk_service_listener = ServiceListner(target=apk_service_listner, args=());
    monkey_service_listener = ServiceListner(target=monkey_service_listner, args=());
    _llxx_client = llxx_client(apk_service_listener, monkey_service_listener);
    _llxx_client._start()
