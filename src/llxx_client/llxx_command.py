# --*coding:utf-8*--
'''
Created on 2016年8月26日

@author: waywings-3
'''

from abc import abstractmethod
import simplejson as json

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
        
    '''
    query listview
    '''
    def queryListView(self):
        self._command['type'] = self.QUERY_TYPE_BY_LISTVIEW
        
    

if __name__ == '__main__':
    click = ClickCommand()
    click.performClickById("com.llxx.service:id/open_toast")
    print click.getCommand()