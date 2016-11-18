# --*coding:utf-8*--
'''
Created on 2016年11月28日

@author: fanxin, eachen
启动Activity
'''

from llxx_plugunit import PlugUnit
from llxx_command import UiSelectAction, TakeSnapshot
from time import sleep
from llxx_pluggroup import PlugGroup
import os

class TestLoginGroup(PlugGroup):
    def __init__(self):
        PlugGroup.__init__(self)
        self.setClassName("登录")
        self.addTestUnit(StartLoginPage())
    
    
class StartLoginPage(PlugUnit):
    
    app = None
    test_count = 0
    def __init__(self):
        self.name = "跳转登录页面"
        self.version = 1.0
        self.description = "启动页面到登录页面"
    
    def run(self):
        
        sleep(1)
        UiSelectAction().performClickTextRect("我的")
        sleep(1)
        UiSelectAction().performClickTextRect("登录")
        sleep(1)
        currendir = os.getcwd()
        TakeSnapshot().takeSnapshot(currendir + "/snapscreen/snapshot.png")
