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
    def __init__(self, llxx_app):
        self.app = llxx_app
        self.name = "测试UI Select基础组件"
        self.version = 1.0
        self.description = "点击Toast，写入文本，获取焦点，获取文本内容"
    
    def run(self):
        self.app.startActivity("com.llxx.socket.MainActivity")
        time.sleep(1)
        # 
        UiSelectAction().text("Toast").performClick()
        
            
        # # 输入文本
        UiSelectAction().id("com.llxx.service:id/username").inputText("大繁星星")
        UiSelectAction().id("com.llxx.service:id/password").inputText("写了个密码")
        
        
        # # 获取清除焦点
        UiSelectAction().id("com.llxx.service:id/password").requestFocus()
        
        time.sleep(2)
        UiSelectAction().id("com.llxx.service:id/password").clearFocus()
        
        # # 长按
        UiSelectAction().text("Toast").performLongClick()

app.addTestUnit(PlugTestUiSelect(app))
app.start()
