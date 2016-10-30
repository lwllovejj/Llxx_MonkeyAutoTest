# --*coding:utf-8*--
'''
Created on 2016年10月30日

@author: fanxin, eachen
@note: 测试ADB
'''
import os
import re

def getAppLanucherActivity():
    pattern = re.compile(r"[a-zA-Z0-9\.]+/[a-zA-Z0-9\.]+")
    out = os.popen("adb shell dumpsys window windows| grep 'name=' | grep '\/'  ").read()
    return pattern.findall(out)[0]

print getAppLanucherActivity()
