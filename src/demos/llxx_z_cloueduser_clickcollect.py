# --*coding:utf-8*--
'''
Created on 2016年10月30日
@author: fanxin, eachen
@note: 尝试获取当前Activity的跳转关系
'''

from llxx_app import llxx_app
from llxx_command import UiSelectAction, TakeSnapshot
from llxx_monitor import llxx_monitorunit_listener
from llxx_monitorcurrentui import llxx_monitorcurrentui

import string

colloct_activity = "com.cloudd.yundiuser.view.activity.MainActivity"
packagename = "com.cloudd.user"
colloct_activity_full = packagename + "/" + colloct_activity
app = llxx_app("com.cloudd.user")

class AppMonitorListener(llxx_monitorunit_listener):
    
    snapshot= TakeSnapshot()
    def hook(self, llxx_result):
        #print llxx_result.getMessage()
        #print llxx_result.getType()
        #print llxx_result.getParams()
        
        #########################################################################
        # 升级相关
        #########################################################################
        if llxx_result.getType() == "ui_update":
            print "ui更新"
  
app.addMonitorUnit(llxx_monitorcurrentui(AppMonitorListener()))

def toMainActivity():
    topActivity = app.getTopActivity()
    print topActivity
    if colloct_activity_full != topActivity:
        ## 在当前的APP，但是不是主Activity
        if string.find(topActivity, packagename) != -1:
            app.doBack()
            isSucess = app.waitingActivity(colloct_activity)
            if isSucess == False:
                toMainActivity()
        
        ### 在其他的APP中
        else:
            print "准备启动 -> " + colloct_activity
            app.startApp()
            isSucess = app.waitingActivity(colloct_activity)
            if isSucess == False:
                toMainActivity()
toMainActivity()
print "已启动:" + colloct_activity
# # 开始测试
app.run()
