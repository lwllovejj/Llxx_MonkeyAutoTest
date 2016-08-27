# --*coding:utf-8*--
'''
Created on 2016年8月27日

@author: fanxin, eachen
'''
import os
curPath = os.path.abspath(os.path.dirname(__file__))
os.system("adb shell uiautomator dump /data/local/tmp/uidump.xml");
os.system("adb pull /data/local/tmp/uidump.xml .")
os.system("python " + curPath +"/xmltoJson.py -t xml2json -o uidump.json uidump.xml")
os.system("python " + curPath + "/jsonformat.py uidump.json")
