# --*coding:utf-8*--
'''
Created on 2016年11月28日

@author: fanxin, eachen
组件测试
'''

from llxx_command import UiSelectAction
from llxx_monitor import llxx_monitorunit
from time import sleep


class MonitorLocationDialog(llxx_monitorunit):
    
    app = None
    lastWindowsId = 0
    def __init__(self):
        llxx_monitorunit.__init__(self)
        self.name = "当前位置不支持提示"
        self.version = 1.0
        self.description = "当前定位城市不开放出租服务，已帮您定位到昆明市中心"
        self.setAction("start_dialog")
        self.setTimeOut(0)

    def onMonitor(self, message):
        node = message.findnode("说明")
        node_know = message.findnode("知道了")
        # print message.getMessage()
        if node != None and node_know != None:
            # print message.getMessage()
            currentWindowsid = message.getRootWindowsId()
            if self.lastWindowsId == currentWindowsid:
                return
            
            self.lastWindowsId = currentWindowsid
            self.hookApp()
        
    def run(self):
        sleep(0.2)
        # 
        UiSelectAction().text("知道了").performClick()
        
        sleep(1)
