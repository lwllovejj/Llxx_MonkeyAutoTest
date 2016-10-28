# --*coding:utf-8*--
'''
Created on 2016年10月27日

@author: fanxin, eachen
'''
import time

from llxx_app import llxx_app
from llxx_plugunit import PlugUnit
app = llxx_app("com.cloudd.user")

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

## 添加测试单元
app.addTestUnits(PlugUnit())

## 开始测试
app.run()
time.sleep(60)
