# --*coding:utf-8*--
'''
Created on 2016年8月26日

@author: fanxin, eachen
'''

from abc import abstractmethod
import simplejson as json
import os
from fileinput import filename
import types

class command:
    
    def __init__(self):
        self._command= {
            'action': self.getAction()
        }
        
    '''
    get command
    '''
    def getCommand(self):
        return json.dumps(self._command, sort_keys=True) + "}"
    
    @abstractmethod
    def getAction(self):pass

'''
click
'''
class ClickCommand(command):
    
    def __init__(self):
        command.__init__(self)
        self.CLICK_TYPE_BY_NONE = 0x00
        self.CLICK_TYPE_BY_ID = 0x01
        self.CLICK_TYPE_BY_NAME = 0x02
    
        self.CLICK_TYPE_BY_ID_INDEX = 0x03
        self.CLICK_TYPE_BY_NAME_INDEX = 0x04

        
    
    def getAction(self):
        return "preformClick"
    
    '''
    click by id
    '''
    def performClickById(self, idName):
        self._command['clicktype'] = self.CLICK_TYPE_BY_ID
        self._command['name'] = idName
        
    '''
    click by name
    '''
    def performClickByName(self, name):
        self._command['clicktype'] = self.CLICK_TYPE_BY_NAME
        self._command['name'] = name


'''
query
'''
class QueryCommand(command):
    
    def __init__(self):
        command.__init__(self)
        self.QUERY_TYPE_BY_NONE = 0x00
        self.QUERY_TYPE_BY_LISTVIEW = 0x01

        
    
    def getAction(self):
        return "queryAccessibility"
    
    '''
    query none for test
    '''
    def queryNone(self):
        self._command['type'] = self.QUERY_TYPE_BY_NONE
    
    def safeDelFile(self, fildpath, filename):
        targetFile = os.path.join(fildpath,  filename)      
        if os.path.isfile(targetFile): 
            os.remove(targetFile)
    
    def findJsonNode(self, msg, key, value, lists):
        target = msg;
        if type(target) == types.DictType:
            if key in target.keys() and target[key] == value:
                lists.append(target)
            if 'node' in target.keys():
                self.findJsonNode(target['node'], key, value, lists)
        if type(target) == types.ListType:
            for _target in target:
                self.findJsonNode(_target, key, value, lists)
                
    def queryHierarchy(self):
        self.safeDelFile("",  "uidump.json")
        self.safeDelFile("",  "uidump.xml")
        os.system("python ../dump/dumpsnap.py")
        file_object = open('uidump.json')
        try:
            all_the_text = file_object.read()
            target = json.JSONDecoder().decode(all_the_text)
            all_the_text = target["hierarchy"]
            all_the_text = json.dumps(all_the_text, sort_keys=True, indent=4)
        finally:
            file_object.close( )
        message = json.JSONDecoder().decode(all_the_text)
        return message
    '''
    query listview
    '''
    def queryListView(self):
        text = self.queryHierarchy()
        lists = []
        self.findJsonNode(text, 'class', "android.widget.ListView", lists)
        return lists
        
    

if __name__ == '__main__':
    click = ClickCommand()
    click.performClickById("com.llxx.service:id/open_toast")
    print click.getCommand()