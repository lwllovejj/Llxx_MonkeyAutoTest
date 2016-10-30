# --*coding:utf-8*--
'''
Created on 2016年10月28日

@author: fanxin, eachen
@summary: 封装单 APP 测试
'''

from llxx_client_wrap import llxx_client_wrap
from llxx_app_context import llxx_app_context
from llxx_setuperror import Llxx_SetupError
from llxx_command import RegPakcages
from llxx_command import AmCommand
from llxx_command import AmOperation
from llxx_pluggroup import PlugGroup

from llxx_wait import llxx_wait
from llxx_monitor import llxx_monitor

class llxx_app:
    
    _pluggroups = []
    _llxx_client_wrap = None
    _packagename = None
    def __init__(self, package):
        self._package = package
        self._packagename = package 
        self._regapp = False
        
        self.stopApp()
        
        self._client = llxx_client_wrap()
        llxx_app._llxx_client_wrap = self._client
        
        self._monitor = llxx_monitor(self._client)
        
        self._context = llxx_app_context(self._client, self._package)
        
        self._defgroup = PlugGroup(self._client)
        self._pluggroups.append(self._defgroup)
        ### 添加需要测试的package
        regpackages = RegPakcages(self._client)
        packages = []
        packages.append(package)
        self._regapp = regpackages.regPackages(packages)
        if self._regapp:
            print "init test package : " + package + " ok !!!"
        else:
            raise Llxx_SetupError("reg test package error")
    
    '''
    get TestApplication Context
    '''
    def getContext(self):
        return self._context
        
    ## ========================================================
    ## App Utils
    ## ========================================================    
    def startApp(self):
        am = AmCommand(self._client)
        return am.startApp(self._package)
    
    def stopApp(self):
        am = AmOperation()
        am.stopApp(self._package)
    
    def restartApp(self):
        self.stopApp()
        return self.startApp()
        
    def waitingActivity(self, activityname):
        return llxx_wait(self._client).waitForActivity(activityname)
    
    ## ========================================================
    ## Test 
    ## ========================================================
    '''
    add monitor
    '''
    def addMonitorUnit(self, unit):
        self._monitor.addMonitorUnit(unit)
        
    '''
    remove monitor
    '''
    def removeMonitorUnit(self, unit):
        self._monitor.removeMonitoUnit(unit)
    ## ========================================================
    ## Test 
    ## ========================================================
    '''
    add test group
    '''
    def addTestGroup(self, group):
        self._pluggroups.append(group)
    
    '''
    add test units to def group
    '''
    def addTestUnits(self, unit):
        self._defgroup.addTestUnits(unit)
    
    def addTestPlugs(self, name):
        self._defgroup.addTestPlugs(name)
        
    '''
    '''
    def run(self):
        for group in self._pluggroups:
            group.run()
if __name__ == '__main__':
    pass