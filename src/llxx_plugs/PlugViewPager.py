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

__all__ = ["PlugTestViewparger"]
class PlugTestViewparger(PlugUnit):
    
    def __init__(self):
        self.name = "testviewpager"
        self.version = 1.0
        self.description = "test viewpager and click"
    
    def run(self, llxx_client):
        print "test view pager"
        query = UiSelectQuery(llxx_client)
        listview = query.className("android.support.v4.view.ViewPager").query()
        if listview != None:
            print listview
            if listview['isfind']:
                listbound = bounds(listview['node']['bounds'])
                count = 0
                while count < 10:
                    ## print takeSnapshot.takeSnapshot(currendir + "//snapshot_yule" + str(time.time()) +".png")
                    cmd = "adb shell input swipe" + " " + listbound.centerRightToLeft()
                    print cmd
                    os.system(cmd)
                    time.sleep(2)
                    count += 1
                    #duration += 50
                print "test list view end"
        
        