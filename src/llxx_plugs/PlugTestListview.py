# --*coding:utf-8*--
'''
Created on 2016年9月14日

@author: fanxin, eachen
'''
from llxx_plugunit import PlugUnit
from llxx_command import UiSelectQuery
from llxx_node import bounds
import os
import time

__all__ = ["PlugTestListview"]
class PlugTestListview(PlugUnit):
    
    def __init__(self):
        self.name = "testlistview"
        self.version = 1.0
        self.description = "test list view scoller and click"
    
    def run(self, llxx_client):
        print "test list view"
        query = UiSelectQuery(llxx_client)
        listview = query.className("android.widget.ListView").query()
        if listview != None:
            print listview
            if listview['isfind']:
                listbound = bounds(listview['node']['bounds'])
                print "adb shell input swipe " + listbound.centerTopToBottom()
                os.system("adb shell input swipe " + listbound.centerTopToBottom())
                time.sleep(5)
                duration = 100
                count = 0
                while count < 10:
                    ## print takeSnapshot.takeSnapshot(currendir + "//snapshot_yule" + str(time.time()) +".png")
                    cmd = "adb shell input swipe" + " " + listbound.centerBottomToTop() + " " + str(duration)
                    print cmd
                    os.system(cmd)
                    time.sleep(1)
                    count += 1
                    #duration += 50
                print "test list view end"
        
        