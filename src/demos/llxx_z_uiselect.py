# --*coding:utf-8*--
'''
Created on 2016年10月27日

@author: fanxin, eachen
'''

from llxx_app import llxx_app
from llxx_command import UiSelectAction


app = llxx_app("com.llxx.service")

# 
# UiSelectAction().performClickByName("Toast")

# UiSelectAction().performClickById("com.llxx.service:id/open_toast")

UiSelectAction().inputText("com.llxx.service:id/username", "繁星")

# # 开始测试
app.run()
