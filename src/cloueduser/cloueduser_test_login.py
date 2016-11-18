# --*coding:utf-8*--
'''
Created on 2016年11月28日

@author: fanxin, eachen
启动Activity
'''

from llxx_plugunit import PlugUnit
from llxx_command import UiSelectAction
from time import sleep


class TestLogin(PlugUnit):
    
    app = None
    test_count = 0
    def __init__(self):
        self.name = "登录"
        self.version = 1.0
        self.description = "测试登录"
    
    def run(self):
        
        sleep(1)
        UiSelectAction().performClickTextRect("我的")
        sleep(1)
        UiSelectAction().performClickTextRect("登录")
        sleep(1)
