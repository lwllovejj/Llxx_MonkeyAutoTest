# --*coding:utf-8*--
'''
Created on 2016年10月27日

@author: fanxin, eachen
'''
from llxx_app import llxx_app
from llxx_plugunit import PlugUnit
app = llxx_app("com.cloudd.user")

isStartApp = app.startApp()
print "start app sucess : " + str(isStartApp)
activitys = app.getContext().allActivity()['activitys']
for activity in activitys:
    print activity

## 添加测试单元
app.addTestUnits(PlugUnit())

## 开始测试
app.run()
