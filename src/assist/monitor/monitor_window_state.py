# --*coding:utf-8*--
'''
Created on 2016年11月28日

@author: fanxin, eachen
监听窗口变化信息，并打印接收到的信息
'''

from llxx_monitor import llxx_monitorunit


class MonitorWindowState(llxx_monitorunit):
    
    app = None
    lastWindowsId = 0
    def __init__(self):
        llxx_monitorunit.__init__(self)
        self.name = "捕获窗口的数据变化"
        self.version = 1.0
        self.description = "捕获窗口的变化"
        self.setAction("window_state")
        self.setTimeOut(0)

    def onMonitor(self, message):
        print message.getMessage()
        
    def run(self):
        pass
