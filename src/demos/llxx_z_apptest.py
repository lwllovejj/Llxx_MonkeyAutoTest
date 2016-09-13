# --*coding:utf-8*--
'''
Created on 2016年9月12日

@author: fanxin, eachen
'''
from llxx_app import llxx_app
from llxx_plugunit import PlugUnit
app = llxx_app("com.netease.newsreader.activity")

## 添加测试单元
app.addTestUnits(PlugUnit())

app.addTestPlugs("testlistview")

## 开始测试
app.run()
