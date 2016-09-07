# --*coding:utf-8*--
'''
Created on 2016年8月29日

@author: fanxin, eachen
'''

from llxx_command import Query


from llxx_client_wrap import llxx_client_wrap

client = llxx_client_wrap()
query = Query(client)

## 查询当前的Activity是哪个
print query.getTopActivity()

## 查询当前的屏幕尺寸
print query.getScreenSize()

## 查询 com.netease.newsreader.activity 中所有的Activity
print query.getAllActivity("com.netease.newsreader.activity")

# print query.getAllService("com.netease.newsreader.activity")
print query.getAllService("com.llxx.service")

## 查询所有的App信息
print query.getAllAppInfo()
