# --*coding:utf-8*--
'''
Created on 2016年8月28日

@author: fanxin, eachen
'''
import os

from llxx_client_wrap import llxx_client_wrap
from llxx_command import ClickCommand
from llxx_command import QueryCommand
from llxx_wait import llxx_wait
import simplejson as json
import time
    
client = llxx_client_wrap()
click = {}
click["cmd"] = "action"
click["action"] = "scroll"
click["elementId"] = "com.netease.newsreader.activity:id/ry"
params = {}
click["params"] = params
params["startX"] = 120
params["startY"] = 300
params["endX"] = 1080
params["endY"] = 300
params["steps"] = 10

client.sendToUianimator(json.dumps(click, sort_keys=True) + "}")
print "1111"
time.sleep(2)

client.sendToUianimator(json.dumps(click, sort_keys=True) + "}")
print "2222"
time.sleep(2)

client.sendToUianimator(json.dumps(click, sort_keys=True) + "}")
print "3333"
time.sleep(2)

client.sendToUianimator(json.dumps(click, sort_keys=True) + "}")
print "4444"
time.sleep(2)

client.sendToUianimator(json.dumps(click, sort_keys=True) + "}")
print "5555"
time.sleep(2)

client.sendToUianimator(json.dumps(click, sort_keys=True) + "}")
print "6666"
time.sleep(2)

while True:
    time.sleep(2)