# --*coding:utf-8*--
'''
Created on 2016年11月28日

@author: fanxin, eachen
组件测试
'''

from llxx_command import UiSelectAction
import time
from llxx_monitor import llxx_monitorunit
from time import sleep


class TestMonitor(llxx_monitorunit):
    
    app = None
    lastWindowsId = 0
    def __init__(self):
        llxx_monitorunit.__init__(self)
        self.name = "TestMonitor"
        self.version = 1.0
        self.description = "监听打开Dialog"
        self.setAction("start_dialog")
        self.setTimeOut(0)

    def onMonitor(self, message):
        node = message.findnode("对话框信息")
        if node != None:
            print message.getMessage()
            currentWindowsid = message.getRootWindowsId()
            if self.lastWindowsId == currentWindowsid:
                return
            
            self.lastWindowsId = currentWindowsid
            self.hookApp()
        
    def run(self):
        sleep(1)
        # 
        UiSelectAction().text("取消").performClick()
        sleep(1)
