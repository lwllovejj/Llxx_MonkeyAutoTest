# --*coding:utf-8*--
'''
Created on 2016年11月28日

@author: fanxin, eachen
'''

from llxx_app import llxx_app
from llxx_z_testunit_monitor import TestMonitor
from llxx_plugunit import PlugUnit
import time
from llxx_command import UiSelectAction

app = llxx_app("com.llxx.service")
app.setReportPath("ts1.html")

app.addMonitorUnit(TestMonitor())

class PlugTestUiSelect(PlugUnit):
    
    app = None
    index = 0
    def __init__(self, llxx_app):
        self.app = llxx_app
        self.name = "测试点击Toast"
        self.version = 1.0
        self.description = "点击Toast"
    
    def run(self):
        self.app.startActivity("com.llxx.socket.MainActivity")
        time.sleep(1)
        UiSelectAction().text("Toast").performClick()

app.addTestUnit(PlugTestUiSelect(app))
app.start()
