# --*coding:utf-8*--
'''
Created on 2016年11月28日

@author: fanxin, eachen
启动Activity
'''

from llxx_plugunit import PlugUnit


class StartMain(PlugUnit):
    
    app = None
    test_count = 0
    def __init__(self):
        self.name = "启动App"
        self.version = 1.0
        self.description = "启动主页"
    
    def run(self):
        
        print "=="
        isStartApp = self.getApp().restartApp()
        if not isStartApp:
            print "启动APP失败，请确认APP已经安装"
            exit(1)
        else:
            print "已启动APP"
        
        self.getApp().waitingActivity("com.cloudd.yundiuser.view.activity.MainActivity")
