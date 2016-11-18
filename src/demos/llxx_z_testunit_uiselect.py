# --*coding:utf-8*--
'''
Created on 2016年11月28日

@author: fanxin, eachen
组件测试
'''

from llxx_command import UiSelectAction
import time
from llxx_plugunit import PlugUnit


class PlugTestUiSelect(PlugUnit):
    
    app = None
    test_count = 0
    def __init__(self, llxx_app):
        self.app = llxx_app
        self.name = "testuiselect"
        self.version = 1.0
        self.description = "测试 ui select"
    
    def run(self):
        self.app.startActivity("com.llxx.socket.MainActivity")
        time.sleep(1)
        # 
        UiSelectAction().text("Toast").performClick()
        
        # UiSelectAction().performClickById("com.llxx.service:id/open_toast")
        self.test_count += 1
        
        if self.test_count < 5:
            UiSelectAction().text("弹出对话框").performClick()
            time.sleep(1)
            
        # # 输入文本
        UiSelectAction().id("com.llxx.service:id/username").inputText("大繁星星")
        UiSelectAction().id("com.llxx.service:id/password").inputText("写了个密码")
        
        
        # # 获取清除焦点
        UiSelectAction().id("com.llxx.service:id/password").requestFocus()
        
        time.sleep(2)
        UiSelectAction().id("com.llxx.service:id/password").clearFocus()
        
        # # 长按
        UiSelectAction().text("Toast").performLongClick()
