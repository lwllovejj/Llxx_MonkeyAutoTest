# --*coding:utf-8*--
'''
Created on 2016年10月27日

@author: fanxin, eachen
'''

from llxx_app import llxx_app
from llxx_command import Query

app = llxx_app("com.llxx.service")
print Query().getAllActivity("com.llxx.service")

print Query().getAllAppInfo()