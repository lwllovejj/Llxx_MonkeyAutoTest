# --*coding:utf-8*--
'''
Created on 2016年8月26日

@author: lwllovewf2010
'''
from llxx_client import llxx_client
from llxx_client import llxx_client_listner
from llxx_command import ClickCommand
from llxx_wait import llxx_wait
import os

showtoast = False;
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

class llxx_client_wrap(llxx_client_listner):
    
    messageListeners = []
    def __init__(self):
        self._llxx_client = llxx_client(self.apk_service_listener, self.monkey_service_listener);
        self._llxx_client._start()
        
    def onMessage(self, message):
        #print ("receive message -> " + message)
        #target = json.JSONDecoder().decode(message)  
        #print target['action']  
        self._target(message)
    
    def apk_service_listener(self, message):
        global showtoast
        print ("apk_service receive message -> " + message)
        
        ## send to reg client
        for listener in self.messageListeners:
            listener.onMessage(message);
            
        target = json.JSONDecoder().decode(message)  
        if target['action'] == "notify":
            showtoast = target['classname'] == "android.widget.Toast$TN"
            print showtoast

    def monkey_service_listener(self, message):
            print ("monkey_service receive message -> " + message)
            target = json.JSONDecoder().decode(message)  
            print target['action']  
    '''
    send message to Android Apk Service
    '''
    def sendToService(self, msg):
        self._llxx_client.sendToService(msg)
        
    '''
    send message to MonkeyRunner Service
    '''
    def sendToMonkeyRunner(self, msg):
        self.socket_monkeyrunner.send(msg);
    
    def runCommand(self, command):
        self.sendToService(click.getCommand())
        
    def regMessageListner(self, listener):
        self.messageListeners.append(listener)
    
    def unRegMessageListener(self, listener):
        self.messageListeners.remove(listener)
    
if __name__ == '__main__':
    os.system("adb forward tcp:8082 tcp:8082")
    
    client = llxx_client_wrap()
    print "------------"
    click = ClickCommand()
    # click.performClickById("com.llxx.service:id/open_toast")
    # click.performClickByName(u"启动第二页")
    # waitActivity = llxx_wait("com.llxx.servic", client);
    # client.runCommand(click)
    # waitActivity.waitForActivity("")
    
    click.performClickByName(u"Show_Toast")
    
    waitToast = llxx_wait("com.llxx.servic", client);
    client.runCommand(click)
    isMatch = waitToast.waitForNotifyToast(u"show toast")
    if isMatch:
        print "waitForNotifyToast ok"
        exit(0)
    
        