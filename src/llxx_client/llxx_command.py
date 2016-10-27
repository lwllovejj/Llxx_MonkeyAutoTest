# --*coding:utf-8*--
'''
Created on 2016年8月26日

@author: fanxin, eachen
'''

from abc import abstractmethod
import simplejson as json
import os
import time
from llxx_wait import llxx_wait
import types

PHONE_WORKSPACE = "/sdcard/llxx/";

class command:
    
    def __init__(self):
        self._command = {
            'action': self.getAction()
        }
        self._params = {
        
        }
    '''
    get command
    '''
    def getCommand(self):
        self._command['params'] = self._params
        return json.dumps(self._command, sort_keys=True)
    
    '''
    get command
    '''
    def getCommandNoApadd(self):
        self._command['params'] = self._params
        return json.dumps(self._command, sort_keys=True)
    
    @abstractmethod
    def getAction(self):pass

    '''
    wait service return action result
    '''
    def priviteWaitParams(self, client_wrap):
        issend = client_wrap.runCommand(self)
        if issend == False:
            return False
        result = llxx_wait(client_wrap).waitForParams(self._command, 10)
        if result != None and result['sucess']:
            if 'params' in result.keys():
                return result['params']
            return True
        return False
    
    '''
    
    '''
    def runShellCommand(self, command):
        tmp = os.popen("adb shell " + command).readlines()
        return tmp

    def runSysCommand(self, command):
        tmp = os.popen(command).readlines()
        return tmp
'''
click
'''
class ClickCommand(command):
    
    def __init__(self, client_wrap):
        command.__init__(self)
        self.client_wrap = client_wrap
        
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
        self._params['clicktype'] = self.CLICK_TYPE_BY_ID
        self._params['name'] = idName
        self.priviteWaitParams(self.client_wrap)
        
    '''
    click by name
    '''
    def performClickByName(self, name):
        self._params['clicktype'] = self.CLICK_TYPE_BY_NAME
        self._params['name'] = name
        return self.priviteWaitParams(self.client_wrap)
    
    '''
    click by name index
    '''
    def performClickByNameIndex(self, name, index):
        self._params['clicktype'] = self.CLICK_TYPE_BY_NAME_INDEX
        self._params['name'] = name
        self._params['index'] = index
        return self.priviteWaitParams(self.client_wrap)
    
class RegPakcages(command):
    
    def __init__(self, client_wrap):
        command.__init__(self)
        self.client_wrap = client_wrap
    
    def getAction(self):
        return "regPackage"

    def priviteWaitParams(self):
        issend = self.client_wrap.runCommand(self)
        if issend == False:
            return False
        result = llxx_wait(self.client_wrap).waitForParams(self._command, 10)
        if result != None and result['sucess']:
            if 'params' in result.keys():
                return result['params']
            return True
        return False
    
    def regPackages(self, packages):
        self._params['packages'] = packages
        return self.priviteWaitParams()

class TakeSnapshot(command):
    
    def __init__(self, client_wrap):
        command.__init__(self)
        self.client_wrap = client_wrap
    
    def getAction(self):
        return "takesnapshot"

    def priviteWaitParams(self):
        issend = self.client_wrap.runMonkeyCommand(self)
        if issend == False:
            return False
        result = llxx_wait(self.client_wrap).waitForParams(self._command, 10)
        if result != None and result['sucess']:
            if 'params' in result.keys():
                return result['params']
            return True
        return False
    
    def takeSnapshot(self, filepath):
        self._params['filepath'] = filepath
        self.runShellCommand("mkdir -p " + PHONE_WORKSPACE + "/snap/")
        filetemp = PHONE_WORKSPACE + "/snap/snap_" + str(time.time()) + ".png";
        self.runShellCommand("screencap -p " + filetemp)
        self.runSysCommand("adb pull " + filetemp + " " + filepath)
        return os.path.isfile(filepath)
'''
operation
'''
class AmOperation(command):
    def __init__(self):
        command.__init__(self)
        self._debug = False
        
    def startApp(self, package):
        command = "adb shell am start " + str(package)
        
        if self._debug :
            print command
            
        self.runSysCommand(command)

'''
operation
'''
class SysOperation(command):
    def __init__(self):
        command.__init__(self)
        
    def reboot(self):
        self.runSysCommand("adb reboot")
    
    def watchprops(self):
        self.runShellCommand("watchprops")
        
'''
query
'''
class AmCommand(command):
    
    def __init__(self, client_wrap):
        command.__init__(self)
        self.client_wrap = client_wrap
        
    
    def getAction(self):
        return "am"
    
    '''
    start app 
    '''
    def startApp(self, pacakge):
        self._command['type'] = 'start_app'
        self._command['packagename'] = pacakge
        return self.priviteWaitParams(self.client_wrap)
    
'''
query
'''
class Query(command):
    
    def __init__(self, client_wrap):
        command.__init__(self)
        self.client_wrap = client_wrap
    
    def getAction(self):
        return "query"
    
    def priviteWaitParams(self):
        self.client_wrap.runCommand(self)
        result = llxx_wait(self.client_wrap).waitForParams(self._command, 10)
        if result != None and result['sucess']:
            return result['params']
        return None
    
    def getTopActivity(self):
        self._command['type'] = 'top_activity'
        result = self.priviteWaitParams()
        
        if result != None:
            return result['class']
        return None
    
    '''
    get screen size
    @return: result['width':width, 'height':height]
    '''
    def getScreenSize(self):
        self._command['type'] = 'screensize'
        result = self.priviteWaitParams()
        
        if result != None:
            return result
        return None
    '''
    get package all Activity
    @return: {'activitys': [{'name': 'xxx.xxx.xxx.Activity1'}, {'name': 'xxx.xxx.xxx.Activity2'}]}
    '''
    def getAllActivity(self, package):
        self._command['type'] = 'allactivity'
        self._params['package'] = package
        result = self.priviteWaitParams()
        
        if result != None:
            return result
        return None
    
    
    def getAllService(self, package):
        self._command['type'] = 'allservice'
        self._params['package'] = package
        result = self.priviteWaitParams()
        
        if result != None:
            return result
        return None
        
    def getAllAppInfo(self):
        self._command['type'] = 'allappinfo'
        self._params['dir'] = '/sdcard/llxx/'
        result = self.priviteWaitParams()
        
        if result != None:
            return result
        return None


SELECTOR_NIL = 0
SELECTOR_TEXT = 1
SELECTOR_START_TEXT = 2
SELECTOR_CONTAINS_TEXT = 3
SELECTOR_CLASS = 4
SELECTOR_DESCRIPTION = 5
SELECTOR_START_DESCRIPTION = 6
SELECTOR_CONTAINS_DESCRIPTION = 7
SELECTOR_INDEX = 8
SELECTOR_INSTANCE = 9
SELECTOR_ENABLED = 10
SELECTOR_FOCUSED = 11
SELECTOR_FOCUSABLE = 12
SELECTOR_SCROLLABLE = 13
SELECTOR_CLICKABLE = 14
SELECTOR_CHECKED = 15
SELECTOR_SELECTED = 16
SELECTOR_ID = 17
SELECTOR_PACKAGE_NAME = 18
SELECTOR_CHILD = 19
SELECTOR_CONTAINER = 20
SELECTOR_PATTERN = 21
SELECTOR_PARENT = 22
SELECTOR_COUNT = 23
SELECTOR_LONG_CLICKABLE = 24
SELECTOR_TEXT_REGEX = 25
SELECTOR_CLASS_REGEX = 26
SELECTOR_DESCRIPTION_REGEX = 27
SELECTOR_PACKAGE_NAME_REGEX = 28
SELECTOR_RESOURCE_ID = 29
SELECTOR_CHECKABLE = 30
SELECTOR_RESOURCE_ID_REGEX = 31
class UiSelectQuery(command):
    
    def __init__(self, client_wrap):
        command.__init__(self)
        self.client_wrap = client_wrap
        self._select = {}

    
    def getAction(self):
        return "queryAccessibility"
    
    def query(self):
        self._params['select'] = self._select
        result = self.priviteWaitParams(self.client_wrap)
        
        if result != None:
            return result
        return None
    
    def className(self, classname):
        self._select[str(SELECTOR_CLASS)] = classname
        return self
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
        targetFile = os.path.join(fildpath, filename)      
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
        # {'index': '1', 'selected': 'false', 'checked': 'false', 'package': 'com.netease.newsreader.activity', 
        # 'focusable': 'false', 'long-clickable': 'false', 'enabled': 'true', 'bounds': '[0,0][1080,78]', 
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
        self.safeDelFile("", "uidump.json")
        self.safeDelFile("", "uidump.xml")
        os.system("python ../dump/dumpsnap.py")
        file_object = open('uidump.json')
        try:
            all_the_text = file_object.read()
            target = json.JSONDecoder().decode(all_the_text)
            all_the_text = target["hierarchy"]
            all_the_text = json.dumps(all_the_text, sort_keys=True, indent=4)
        finally:
            file_object.close()
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
        
# #regPackage        
        
if __name__ == '__main__':
    click = ClickCommand()
    click.performClickById("com.llxx.service:id/open_toast")
    print click.getCommand()
