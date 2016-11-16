# --*coding:utf-8*--
'''
Created on 2016年10月27日

@author: fanxin, eachen
'''

from llxx_app import llxx_app
from llxx_command import UiSelectAction

app = llxx_app("com.llxx.service")

app.startActivity("com.llxx.socket.MainActivity")

# 
UiSelectAction().text("Toast_").performClick()

## 停止，退出测试
app.stop()
