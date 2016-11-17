# --*coding:utf-8*--
'''
Created on 2016年10月28日

@author: fanxin, eachen
@summary: 封装单 APP 测试
'''

from llxx_client_wrap import llxx_client_wrap
from llxx_app_context import llxx_app_context
from llxx_setuperror import Llxx_SetupError
from llxx_command import RegPakcages, SysOperation
from llxx_command import AmCommand
from llxx_command import Query
from llxx_pluggroup import PlugGroup

from llxx_wait import llxx_wait
from llxx_monitor import llxx_monitor
from llxx_report_listener import llxx_report_listener
import time

'''
测试栈，用来管理当前的测试队列
'''
class llxx_test_stack:
    
    
    test_stack = []
    def __init__(self):
        pass
    
    def push_test_unit(self):
        pass
    
class llxx_app(llxx_report_listener):
    
    _pluggroups = []
    _llxx_client_wrap = None
    _packagename = None
    _llxx_report_listener = None
    
    '''
    @param initStopApp: 启动的时候是否强行停止App
    '''
    def __init__(self, package , initStopApp=False):
        self._package = package
        self._packagename = package 
        self._regapp = False
        
        if initStopApp:
            self.stopApp()
        
        self._client = llxx_client_wrap()
        llxx_app._llxx_client_wrap = self._client
        llxx_app._llxx_report_listener = self
        
        self._monitor = llxx_monitor(self._client)
        
        self._context = llxx_app_context(self._client, self._package)
        
        self._defgroup = PlugGroup()
        self._pluggroups.append(self._defgroup)
        self._currentTestUnit = None
        
        # ## 添加需要测试的package
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
    # # App Utils
    ## ========================================================    
    
    '''
    @note: 启动当前的APP
    '''
    def startApp(self):
        am = AmCommand()
        return am.startApp(self._package)
    
    '''
    @note: 停止当前的APP
    '''
    def stopApp(self):
        am = AmCommand()
        am.stopApp(self._package)
    '''
    @note: 重启当前的测试APP
    '''
    def restartApp(self):
        self.stopApp()
        return self.startApp()
    
    '''
    @note: 获取当前运行在最前面的APP
    '''
    def getTopActivity(self):
        return Query().getTopActivity()
    
    '''
    @note: 启动指定的Acitivity
    '''
    def startActivity(self, activityname):
        result = AmCommand().startActivity(self._package, activityname)
        if result:
            return self.waitingActivity(activityname)
        return False
    '''
    @note: 等待指定的Activity启动
    '''
    def waitingActivity(self, activityname):
        return llxx_wait(self._client).waitForActivity(activityname, 10)
    
    ## ========================================================
    # # Keycode
    ## ========================================================
    
    '''
    @note: 返回
    '''
    def doBack(self):
        SysOperation().back()
    
    ## ========================================================
    # # Test 
    ## ========================================================
    '''
    @note: 添加检测单元
    '''
    def addMonitorUnit(self, unit):
        self._monitor.addMonitorUnit(unit)
        
    '''
    remove monitor
    '''
    def removeMonitorUnit(self, unit):
        self._monitor.removeMonitoUnit(unit)
    ## ========================================================
    # # Test 
    ## ========================================================
    '''
    add test group
    '''
    def addTestGroup(self, group):
        self._pluggroups.append(group)
    
    '''
    add test units to def group
    '''
    def addTestUnit(self, unit):
        self._defgroup.addTestUnit(unit)
    
    def addTestPlug(self, name):
        self._defgroup.addTestPlug(name)
        
    '''
    '''
    def start(self):
        for group in self._pluggroups:
            for plug in group.getTestUnits():
                self._currentTestUnit = plug
                unitmsg = "\n==========================================================\n\n"
                unitmsg += "name: " + str(self._currentTestUnit.getName()) + "\n"
                unitmsg += "version: " + str(self._currentTestUnit.getVersion()) + "\n"
                unitmsg += "description: " + self._currentTestUnit.getDescription() + "\n"
                print unitmsg
                plug.run()
                unitmsg = "\n==========================================================\n"
                print unitmsg
                
        self.stop()
        
    '''
    @note: 停止
    '''          
    def stop(self):
        self._monitor.stop()
    
    '''
    @note: 返回失败原因
    '''
    def onReportError(self, errorReason):
        unitmsg = "Fail: " + str(errorReason) + "\n"
        print unitmsg
    
    '''
    @note: 返回成功消息
    '''
    def onReportSucess(self, sucess):
        unitmsg = "Pass: " + str(sucess) + "\n"
        print unitmsg
        
if __name__ == '__main__':
    pass
