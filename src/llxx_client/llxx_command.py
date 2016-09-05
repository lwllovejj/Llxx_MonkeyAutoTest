# --*coding:utf-8*--
'''
Created on 2016年8月26日

@author: fanxin, eachen
'''

from abc import abstractmethod
import simplejson as json
import os
from fileinput import filename
from llxx_wait import llxx_wait
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
class Query(command):
    
    def __init__(self, client_wrap):
        command.__init__(self)
        self.client_wrap = client_wrap
    
    def getAction(self):
        return "query"
    
    def getTopActivity(self):
        self._command['type'] = 'top_activity'
        self.client_wrap.runCommand(self)
        result = llxx_wait(self.client_wrap).waitForParams(self._command, 10)
        if result != None and result['sucess']:
            return result['params']['class']
        return None
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
                lists.append(self._packNodeWithoutChild(target))
            
            if 'node' in target.keys():
                self.findJsonNode(target['node'], key, value, lists)
                
        if type(target) == types.ListType:
            for _target in target:
                self.findJsonNode(_target, key, value, lists)
                
    def _packNodeWithoutChild(self, msg):
        #{'index': '1', 'selected': 'false', 'checked': 'false', 'package': 'com.netease.newsreader.activity', 
        #'focusable': 'false', 'long-clickable': 'false', 'enabled': 'true', 'bounds': '[0,0][1080,78]', 
        # 'content-desc': u'', 'resource-id': 'android:id/statusBarBackground', 'focused': 'false', 'clickable': 
        # 'false', 'checkable': 'false', 'password': 'false', 'text': u'', 'class': 'android.view.View', 'scrollable': 'false'}
        target = {}
        target['index'] = msg['index']
        target['text'] = msg['text']
        
        target['resource-id'] = msg['resource-id']
        target['content-desc'] = msg['content-desc']
        
        target['package'] = msg['package']
        target['class'] = msg['class']
        
        target['selected'] = msg['selected']
        target['checked'] = msg['checked']
        target['focusable'] = msg['focusable']
        target['enabled'] = msg['enabled']
        target['focusable'] = msg['focusable']
        target['bounds'] = msg['bounds']
        target['focused'] = msg['focused']
        target['clickable'] = msg['clickable']
        target['checkable'] = msg['checkable']
        target['password'] = msg['password']
        target['scrollable'] = msg['scrollable']
        target['long-clickable'] = msg['long-clickable']
        return target
    
    def _findNodeIdNotNull(self, msg, lists):
        target = msg;
        if type(target) == types.DictType:
            if 'resource-id' in target.keys() and target['resource-id'] != None and target['resource-id'] != '':
                lists.append(self._packNodeWithoutChild(target))
            if 'node' in target.keys():
                self._findNodeIdNotNull(target['node'], lists)
        if type(target) == types.ListType:
            for _target in target:
                self._findNodeIdNotNull(_target, lists)
                
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
        
    '''
    
    '''
    def queryIdNotNull(self):
        text = self.queryHierarchy()
        lists = []
        self._findNodeIdNotNull(text, lists)
        return lists
    
    def queryCanclick(self):
        text = self.queryHierarchy()
        lists = []
        self.findJsonNode(text, 'clickable', "true", lists)
        return lists
        
        
        
if __name__ == '__main__':
    click = ClickCommand()
    click.performClickById("com.llxx.service:id/open_toast")
    print click.getCommand()