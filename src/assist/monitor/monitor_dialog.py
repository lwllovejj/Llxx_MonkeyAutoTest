# --*coding:utf-8*--
'''
Created on 2016年11月18日

@author: fanxin, eachen
监听对话框
'''


from llxx_monitor import llxx_monitorunit


class MonitorDialog(llxx_monitorunit):
    
    app = None
    lastWindowsId = 0
    def __init__(self):
        llxx_monitorunit.__init__(self)
        self.name = "监听对话框弹出"
        self.version = 1.0
        self.description = "监听对话框弹出"
        self.setAction("start_dialog")
        self.setTimeOut(0)

    def onMonitor(self, message):
        print message.getMessage()
        
    def run(self):
        pass
