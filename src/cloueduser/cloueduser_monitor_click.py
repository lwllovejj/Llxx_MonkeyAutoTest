# --*coding:utf-8*--
'''
Created on 2016年11月28日

@author: fanxin, eachen
组件测试
'''

from llxx_monitor import llxx_monitorunit


class MonitorClick(llxx_monitorunit):
    
    app = None
    lastWindowsId = 0
    def __init__(self):
        llxx_monitorunit.__init__(self)
        self.name = "捕获点击事件"
        self.version = 1.0
        self.description = "捕获点击事件"
        self.setAction("click")
        self.setTimeOut(0)

    def onMonitor(self, message):
        #print message.getMessage()
        pass
        
    def run(self):
        pass
