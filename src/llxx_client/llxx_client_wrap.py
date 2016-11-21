# --*coding:utf-8*--
'''
Created on 2016年8月26日

@author: fanxin, eachen
'''
import os
import sys
import time

curPath = os.path.abspath(os.path.dirname(__file__))
sys.path.append(curPath)

from llxx_client import llxx_client
from llxx_client import llxx_client_listner


showtoast = False;
# pip install simplejson

class ServiceListner(llxx_client_listner):
    
    def __init__(self , target=None,
                 args=()):
        self._target = target
        
    def onMessage(self, message):
        # print ("receive message -> " + message)
        # target = json.JSONDecoder().decode(message)  
        # print target['action']  
        self._target(message)

class llxx_client_wrap(llxx_client_listner):
    
    messageListeners = []
    def __init__(self):
        self.debug = False
        
        os.system("adb forward tcp:8082 tcp:8082")
        os.system("adb forward tcp:8083 tcp:8083")
        
        self._llxx_client = llxx_client(self.apk_service_listener);
        self._llxx_client._start()
        time.sleep(1)
        
    def onMessage(self, message):
        # print ("receive message -> " + message)
        # target = json.JSONDecoder().decode(message)  
        # print target['action']  
        self._target(message)
    
    def apk_service_listener(self, message):
        if self.debug:
            print ("apk_service receive message -> " + message)
        
        # # send to reg client
        for listener in self.messageListeners:
            listener.onMessage(message);

    '''
    send message to Android Apk Service
    '''
    def sendToService(self, msg):
        return self._llxx_client.sendToService(msg)
        
    def runCommand(self, command):
        return self.sendToService(command.getCommand())
    
    def runMonkeyCommand(self, command):
        return self.sendToMonkeyRunner(command.getCommandNoApadd())
        
    def regMessageListner(self, listener):
        self.messageListeners.append(listener)
    
    def unRegMessageListener(self, listener):
        self.messageListeners.remove(listener)
