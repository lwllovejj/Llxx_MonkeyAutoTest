# --*coding:utf-8*--
'''
Created on 2016年11月18日

@author: fanxin, eachen
@note: 
'''
import simplejson as json
import types
import string




'''
客户端和服务端传递消息实体
'''
class Message():
    
    message = None
    jsonMessage = None
    def __init__(self, msg):
        self.message = msg
        self.jsonMessage = json.JSONDecoder().decode(msg)
        self.sucess = self.jsonMessage['sucess']
        self.action = self.jsonMessage['action']
        self.params = None
        if 'params' in self.jsonMessage:
            self.params = self.jsonMessage['params']
        
    '''
    @note: 设置是否执行成功
    '''
    def setSucess(self, sucess):
        self.sucess = sucess
        return self
    
    '''
    @note: 是否执行成功
    '''
    def isSucess(self):
        return self.sucess
    
    '''
    @note: 获取当前执行的消息
    '''
    def getMessage(self):
        return self.message
    
    def getParams(self):
        return self.params
    
    def getAction(self):
        return self.action
    
    '''
    @note: 获取根窗口的windows id
    '''
    def getRootWindowsId(self):
        return self.getParams()["node"]["windowId"]
    
    '''
    @note: 
    '''
    def findnode(self, txt):
        return self.__findNode(self.getParams(), txt)
    
    #######################################################################
    # ## 节点查询
    #######################################################################
    def __findNode(self, jsonTarget, text):
        node = None
        if type(jsonTarget) == types.DictType:
            _temtext = jsonTarget["text"].encode('utf-8')
            if string.find(_temtext, text) != -1:
                node = jsonTarget
                return node
    
            if node == None and "node" in jsonTarget and jsonTarget["node"] != None:
                node = self.__findNode(jsonTarget["node"], text)
                if node != None:
                    return node
        
        if type(jsonTarget) == types.ListType:
            for jsontemp in jsonTarget:
                node = self.__findNode(jsontemp, text)
                if node != None:
                    return node
        return node
