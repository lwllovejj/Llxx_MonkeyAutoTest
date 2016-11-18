# --*coding:utf-8*--
'''
Created on 2016年11月28日

@author: fanxin, eachen
组件测试
'''

from llxx_monitor import llxx_monitorunit


class MonitorStartActivity(llxx_monitorunit):
    
    app = None
    lastWindowsId = 0
    def __init__(self):
        llxx_monitorunit.__init__(self)
        self.name = "捕获启动的Activity"
        self.version = 1.0
        self.description = "启动Activity并输出"
        self.setAction("start_activity")
        self.setTimeOut(0)

    def onMonitor(self, message):
        #print message.getMessage()
        print "start activity -->" + message.getClassName()
        
    def run(self):
        pass
