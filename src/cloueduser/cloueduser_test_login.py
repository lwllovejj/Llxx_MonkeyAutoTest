# --*coding:utf-8*--
'''
Created on 2016年11月28日

@author: fanxin, eachen
启动Activity
'''

from llxx_plugunit import PlugUnit
from llxx_command import UiSelectAction, TakeSnapshot, UiAssert
from time import sleep
from llxx_pluggroup import PlugGroup
import os

class TestLoginGroup(PlugGroup):
    def __init__(self):
        PlugGroup.__init__(self)
        self.setClassName("登录")
        self.addTestUnit(StartLoginPage())
        self.addTestUnit(TestLoginButton())
        self.addTestUnit(TestLoginFlow())
    
    
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

class TestLoginButton(PlugUnit):   
    def __init__(self):
        self.name = "验证登录按钮状态"
        self.version = 1.0
        self.description = "验证登录按钮状态的正确性"
        
    def run(self):
        UiAssert().text("登录").appendDescribe("验证默认登录按钮状态是否禁用").assertEnable(False)
        sleep(1)
     
class TestLoginFlow(PlugUnit):
    
    test_count = 0
    def __init__(self):
        self.name = "验证登录流程正确性"
        self.version = 1.0
        self.description = "验证登录流程正确性"
    
    def run(self):
        
        sleep(1)
        UiSelectAction().className("android.widget.EditText").performClick()
        currendir = os.getcwd()
        TakeSnapshot().takeSnapshot(currendir + "/snapscreen/click_phone_snapshot.png")
        
        ## 手机号码格式错误
        UiSelectAction().className("android.widget.EditText").appendDescribe("验证错误的手机号码").inputText("12345678910")
        TakeSnapshot().takeSnapshot(currendir + "/snapscreen/phone_number_invalid_snapshot.png")
        
        ## 验证错误的手机号码
        UiSelectAction().className("android.widget.EditText").appendDescribe("验证正确的手机号码").inputText("13945678910")
        TakeSnapshot().takeSnapshot(currendir + "/snapscreen/phone_number_valid_snapshot.png")
        
