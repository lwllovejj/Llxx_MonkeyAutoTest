# --*coding:utf-8*--
'''
Created on 2016年8月27日

@author: fanxin, eachen
'''
import os
os.system("adb shell uiautomator dump /data/local/tmp/uidump.xml");
os.system("adb pull /data/local/tmp/uidump.xml .")
os.system("python xmltoJson.py -t xml2json -o uidump.json uidump.xml")
os.system("python jsonformat.py uidump.json")
