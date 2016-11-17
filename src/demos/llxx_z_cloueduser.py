# --*coding:utf-8*--
'''
Created on 2016年10月27日

@author: fanxin, eachen
'''

from llxx_app import llxx_app
from llxx_plugunit import PlugUnit

from llxx_monitorupdate import llxx_monitorupdate
from llxx_monitor import llxx_monitorunit_listener

from llxx_command import UiSelectAction, TakeSnapshot, UiSelectQuery
from llxx_z_cloueduser_monitor import llxx_monitor_dialog
from llxx_monitorcurrentui import llxx_monitorcurrentui
from time import time, sleep

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
        if llxx_result.getType() == "update_dialog":
            self.snapshot.takeSnapshot("snapshot_update_dialog.png")
            print "弹出升级提示，点击确定开始下载任务"
            UiSelectAction().text("确定").performClick()
            
        if llxx_result.getType() == "update_dowload_process":
            #print llxx_result.getParams()
            print llxx_result.getParams()["text"]
            
        if llxx_result.getType() == "apk_install":
            self.snapshot.takeSnapshot("snapshot_update_install.png")
            print "准备安装程序"
            UiSelectAction().text("安装").performClick()
            
        if llxx_result.getType() == "apk_install_report":
            self.snapshot.takeSnapshot("snapshot_update_install_report.png")
            
            if llxx_result.getParams()["sucess"]:
                print "安装完成，打开程序"
                UiSelectAction().text("打开").performClick()
        
        #########################################################################
        # 点击定位开始的知道了
        #########################################################################
        if llxx_result.getType() == "llxx_monitor_dialog":
            print "llxx_monitor_dialog"
            self.snapshot.takeSnapshot("snapshot_monitor_dialog.png")
            UiSelectAction().text("知道了").performClick()
            
#             print UiSelectQuery().queryHierarchy()
#             print "==========="
#             
#             list = UiSelectQuery().queryIdNotNull()
#             for item in list :
#                 print item
#                 
#             print "==========="
#             list =  UiSelectQuery().queryCanclick()
#             for item in list :
#                 print item
  
app.addMonitorUnit(llxx_monitorupdate(AppMonitorListener()))
app.addMonitorUnit(llxx_monitor_dialog(AppMonitorListener()))

# 重启APP并且等待主Activity启动时间
isStartApp = app.restartApp()
if not isStartApp:
    print "启动APP失败，请确认APP已经安装"
    exit(1)
else:
    print "已启动APP"

isToMain = app.waitingActivity("com.cloudd.yundiuser.view.activity.MainActivity")
if not isToMain:
    print "跳转失败"
    exit(1)
else:
    print "启动主Activity成功"


# activitys = app.getContext().allActivity()['activitys']
# for activity in activitys:
#     print activity

# # 添加测试单元

# # 开始测试
app.start()
sleep(10)
