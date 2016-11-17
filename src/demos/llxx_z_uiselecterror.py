# --*coding:utf-8*--
'''
Created on 2016年10月27日

@author: fanxin, eachen
'''

from llxx_app import llxx_app
from llxx_command import UiSelectAction
import time
from llxx_plugunit import PlugUnit

app = llxx_app("com.llxx.service")

__all__ = ["test ui select"]
class PlugTestUiSelect(PlugUnit):
    
    def __init__(self):
        self.name = "testuiselect"
        self.version = 1.0
        self.description = "测试点击ui出错之后处理"
        
    def run(self):
        app.startActivity("com.llxx.socket.MainActivity")
        
        # 
        UiSelectAction().text("Toast_没有这个节点").performClick()
        
        # UiSelectAction().performClickById("com.llxx.service:id/open_toast")
        
        # # 输入文本
        UiSelectAction().id("com.llxx.service:id/username").inputText("大繁星星")
        UiSelectAction().id("com.llxx.service:id/password").inputText("写了个密码")
        
        
        # # 获取清除焦点
        UiSelectAction().id("com.llxx.service:id/password").requestFocus()
        
        time.sleep(2)
        UiSelectAction().id("com.llxx.service:id/password").clearFocus()
        
        # # 长按
        UiSelectAction().text("Toast").performLongClick()

app.addTestUnit(PlugTestUiSelect())
app.start()
