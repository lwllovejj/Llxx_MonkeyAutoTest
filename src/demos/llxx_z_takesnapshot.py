# --*coding:utf-8*--
'''
Created on 2016年9月10日

@author: fanxin, eachen
'''
import os
from llxx_command import TakeSnapshot

## 测试截图
from llxx_client_wrap import llxx_client_wrap

client = llxx_client_wrap()
takeSnapshot = TakeSnapshot(client)
currendir = os.getcwd()
print takeSnapshot.takeSnapshot(currendir + "//snapshot.png")
