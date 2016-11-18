# --*coding:utf-8*--
'''
Created on 2016年10月28日

@author: fanxin, eachen
'''
# pip install simplejson
from llxx_client_wrap import llxx_client_wrap

import simplejson as json

import time

import threading
import string

import types
import Queue
from datetime import datetime
from llxx_plugunit import  PlugUnit
from llxx_message import Message
import llxx_report
from llxx_report import reportMessage

class llxx_monitor:
    
    messageList = Queue.Queue()
    monitorunits = []
    def __init__(self, llxx_client_wrap):
        self._llxx_client_wrap = llxx_client_wrap
        self._start = True
        self._debug = False
        
        # 开始连接
        t = threading.Thread(target=self.monitor, args=())
        t.setDaemon(False)
        t.start()
    
    def onMessage(self, message):
        if message.strip() != "":
            self.messageList.put(message)
        # print "llxx_wait onMessage ->" + message
    
        # # 等待指定的数据
    '''
    @param maps: 对应数据字典
    @param timeout: 超时时间
    '''
    def monitor(self):
        self._llxx_client_wrap.regMessageListner(self)
        
        #starttime = datetime.now()
        while self._start:
            
            ## 1.获取message
            ## 2.解析msg
            ## 3.找合适的单元分发消息
            ## 4. 
            try:
                msg = self.messageList.get(True, 1)
                
            except Exception, ex:
                pass
                
            #endtime = datetime.now()
            # print "units size = " + str(len(self.monitorunits))
            # 配置开始和结束至少30ms以上
            #if len(self.monitorunits) == 0 and (endtime - starttime).seconds > 30:
            #    print "----> no units, monitor now stop"
            #    self._start = False
            #    break
            
            if msg == None:
                continue
            
            # 解析信息
            message = Message(msg)
            timeoutunits = []
            for monitor_unit in self.monitorunits:
                try:
                    # ## 不处理已经超时的模块
                    if monitor_unit.isTimeOut():
                        timeoutunits.append(monitor_unit)
                    
                    # ## 只处理没有超时的模块
                    else:
                        ## 
                        if monitor_unit.getAction() == message.getAction():
                            monitor_unit.onMonitor(message)
                    
                    # ## FOR DEBUG
                    if self._debug:
                        print msg
                        
                except Exception, ex:
                    print Exception, ":", ex
                    
            # ## 移除已经超时的模块
            for monitor_unit in timeoutunits:
                try:
                    self.monitorunits.remove(monitor_unit)
                    
                except Exception, ex:
                    print Exception, ":", ex
            
        self._llxx_client_wrap.unRegMessageListener(self)
    
    '''
    add monitor unit
    '''
    def addMonitorUnit(self, llxx_monitorunit):
        llxx_monitorunit.initMonitor(self)
        self.monitorunits.append(llxx_monitorunit)
    
    '''
    remote monitor unit
    '''
    def removeMonitoUnit(self, llxx_monitorunit):
        self.monitorunits.remove(llxx_monitorunit)

    def start(self):
        self._start = True
        
    def stop(self):
        self._start = False
        
    def setDebug(self, debug):
        self._debug = debug

'''
监听单元最后会回馈信息到这个地方
'''    
class llxx_monitorunit_listener:
    def hook(self, llxx_result):
        pass

'''
monitorunit 的返回结果封装
''' 
class llxx_result:
    
    def __init__(self, message, msg_type, params):
        self._message = message
        self._type = msg_type
        self._params = params
        
    def getMessage(self):
        return self._message
    
    def getType(self):
        return self._type
    
    def getParams(self):
        return self._params
'''
监测单元
''' 
class llxx_monitorunit(PlugUnit):  
    
    action = ""
    def __init__(self):
        
        self.starttime = datetime.now()  # 开始时间，会在初始化的时候自动设置
        self.timeout = 30  # 超时时间默认设置为60ms，如果60没有等待到的话就自动被移除了
        self._monitor = None
    
    
    def onMonitor(self, message):
        pass
    
    # ## 回调
    def hookApp(self):
        # 开始连接
        t = threading.Thread(target=self.publishRun, args=())
        t.setDaemon(True)
        t.start()
    
    #######################################################################
    # ## 事件流
    #######################################################################
    def initMonitor(self, monitor):
        self._monitor = monitor
        self.starttime = datetime.now()
    
    '''
    @note: 获取超时时间
    '''
    def getTimeOut(self):
        return self.timeout
    
    '''
    @note: 设置超时时间
    @param timeout: 超时时间 ,0代表永不超时
    '''
    def setTimeOut(self, timeout):
        self.timeout = timeout
    
    '''
    @note: 当前是否已经超时
    '''
    def isTimeOut(self):
        if self.getTimeOut() == 0:
            return False
        # debug
        # print (datetime.now() - self.starttime).seconds
        # print self.getTimeOut()
        return (datetime.now() - self.starttime).seconds > self.getTimeOut()
    
    '''
    @note: 从当前的监听器组合中移除自己
    @param None
    '''
    def remove(self):
        self._monitor.removeMonitoUnit(self)
    
    '''
    @note: 添加下一个监听器，这个的目的主要是用来移除当前的事件之后添加处理下一个事件
    @param llxx_monitorunit: 下一个监听器
    '''
    def addNextMonitor(self, llxx_monitorunit):
        self._monitor.addMonitorUnit(llxx_monitorunit)
    
    '''
    @note: 内部开始执行方法
    '''
    def publishRun(self):
        report = reportMessage().setMsgType(llxx_report.REPORT_MSG_TYPE_IN_MONITOR)
        llxx_report.sendMessageToApp(report)
        self.run()
        report.setMsgType(llxx_report.REPORT_MSG_TYPE_OUT_MONITOR)
        llxx_report.sendMessageToApp(report)
            
    '''
    @note: 设置动作
    '''
    def setAction(self, action):
        self.action = action
    
    '''
    @note: 获取当前检测器要拦截的动作，一个检测器只能拦截一种类型的动作
    '''
    def getAction(self):
        return self.action
    
    '''
    @note: 查找指定的节点
    '''
    def findTextNode(self, msg, text):
        target = json.JSONDecoder().decode(msg)
        return self.findNode(target["params"], text)
    
if __name__ == '__main__':
    monitor = llxx_monitor(llxx_client_wrap())
    
