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
import threading
import Queue
from llxx_report import reportMessage
import llxx_command_control
import llxx_report
from time import sleep
from output_html import OutPutReport, TestReportUnit
import output_html
import time_utils

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
    _llxx_command_control = None
    reportMessageList = Queue.Queue()
    
    isInMonitor = False
    
    _report = None
    
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
        
        # # 命令控制
        self._command_control = llxx_command_control.llxx_command_control()
        llxx_app._llxx_command_control = self._command_control
        
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
        if self.isCommandPass():
            return False
        
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
    
    # ## 测试报告
    def setReportPath(self, path):
        self._report = OutPutReport(path)
        print self._report 

    '''
    @note: 添加报告单元
    '''
    def addReportUnit(self, unit):
        if self._report != None:
            self._report.addTestReport(unit)
    
    '''
    @note: 设置程序的启动时间
    '''
    def setTestStartTile(self):
        if self._report != None:
            self._report.setStartTime()
            
    '''
    @note: 打印报告
    '''
    def outputReport(self):
        if self._report != None:
            self._report.printReport()
            print "output report sucess"
            
    # ## 测试用例
    
    def testUnit(self, plug, testNum):
        # # 表示是否可以跳出这个测试，如果可以则跳出这个测试
        isCanPass = False
        reportmessages = ""
        while not isCanPass:
            
            # # 如果当前在检测中，则开始休眠
            while self.isInMonitor:
                sleep(2)
            
            reportmessages = ""
            innerIsInMonitor = False
            index = 1
            unitmsg = "\n==========================================================\n\n"
            unitmsg += "name: " + str(self._currentTestUnit.getName()) + "\n"
            unitmsg += "version: " + str(self._currentTestUnit.getVersion()) + "\n"
            unitmsg += "description: " + self._currentTestUnit.getDescription() + "\n"
            print unitmsg
            
            # # clean status
            self._command_control.setPass(plug.getName(), False)
            plug.setSucess(True)
            
            # # start test 
            t = threading.Thread(target=plug.run, args=())
            t.setName(plug.getName())
            t.setDaemon(True)
            t.start()
            
            
            isfinish = False
            while True:
                try:
                    message = None
                    message = self.reportMessageList.get(True, 1);
                except:
                    pass
                
                if message != None:
                    if message.getType() == llxx_report.REPORT_MSG_TYPE_TEST_STATUS:
                        if message.isSucess() and not isfinish:
                            print "pass:" + message.getMessage()
                            reportmessages += str(index) + "." + " -> pass" + message.getMessage() + "\n"
                            
                        else:
                            if not isfinish:
                                print "fail:" + message.getMessage()
                                reportmessages += str(index) + "." + " -> fail" + message.getMessage() + "\n"
                                isfinish = True
                                plug.setSucess(False)
                                self._command_control.setPass(t.getName(), True)
                        
                        index += 1
                        
                    # # 当进入监控之后就不处理消息了
                    elif message.getType() == llxx_report.REPORT_MSG_TYPE_IN_MONITOR:
                        print "REPORT_MSG_TYPE_IN_MONITOR"
                        innerIsInMonitor = True
                        self._command_control.setPass(t.getName(), True)
                    
                    elif message.getType() == llxx_report.REPORT_MSG_TYPE_OUT_MONITOR:
                        print "REPORT_MSG_TYPE_OUT_MONITOR"
                    
                # # 如果线程执行完成则退出循环
                if not t.isAlive():
                    break
            
            unitmsg = "\n==========================================================\n"
            print unitmsg
            
            # # 确认是否退出当前测试
            if not innerIsInMonitor:
                isCanPass = True
        
        return reportmessages       
        
    '''
    '''
    def start(self):
        
        self.setTestStartTile()
        
        for group in self._pluggroups:
            for plug in group.getTestUnits():
                
                reportmessages = ""
                self._currentTestUnit = plug
                startTime = time_utils.getTime()
                for i in range(0, plug.getTestCount()):
                    reportmessages = ""
                    exception = False
                    try:
                        reportmessages = self.testUnit(plug, i)
                    except Exception, ex:
                        exception = True
                        
                    #### 填写报告
                    passTime = time_utils.getTime() - startTime
                    try:
                        reportmessages = reportmessages.decode("utf-8", 'replace')
                    except Exception, ex:
                        print "decode fail"
                        
                    report = TestReportUnit()
                    report.setClass(plug.getName().decode("utf-8", 'replace'))
                    report.setName(plug.getDescription().decode("utf-8", 'replace'))
                    if exception:
                        report.setStatus(TestReportUnit.ERROR)
                        
                    elif plug.isSucess():
                        report.setStatus(TestReportUnit.PASS)
                        
                    else :
                        report.setStatus(TestReportUnit.FAIL)
                        
                    report.setMessage(reportmessages)
                    report.setTime(passTime)
                    self.addReportUnit(report)
        sleep(1)  
        self.outputReport()   
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
        self.reportMessageList.put(reportMessage().setSucess(False).setMessage(errorReason)) 
    
    '''
    @note: 返回成功消息
    '''
    def onReportSucess(self, sucess):
        self.reportMessageList.put(reportMessage().setSucess(True).setMessage(sucess)) 
    
    def isCommandPass(self):
        return llxx_command_control.isCommandPass()
    
    def sendMessage(self, message):
        
        # # 当进入监控之后就不处理消息了
        if message.getType() == llxx_report.REPORT_MSG_TYPE_IN_MONITOR:
            self.isInMonitor = True
            if not self._currentTestUnit == None:
                self._currentTestUnit.setReStartByMonitor(True)
            pass
        
        elif message.getType() == llxx_report.REPORT_MSG_TYPE_OUT_MONITOR:
            self.isInMonitor = False
            if not self._currentTestUnit == None:
                self._currentTestUnit.setReStartByMonitor(False)
            pass
        
        self.reportMessageList.put(message) 
    
if __name__ == '__main__':
    pass
