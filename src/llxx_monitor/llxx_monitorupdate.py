# --*coding:utf-8*--
'''
Created on 2016年10月28日

@author: fanxin, eachen
'''
# pip install simplejson
from llxx_monitor import llxx_monitorunit
from llxx_monitor import llxx_monitor

import string


class llxx_monitorupdate(llxx_monitorunit):  
    
    def onMonitor(self, message):
        isHasUpate = string.find(message, "发现新版本，是否升级？") != -1
        if isHasUpate:
            print "发现新版本，是否升级？"
            # print message
        pass
    
if __name__ == '__main__':
    monitor = llxx_monitor()
    monitor.addMonitorUnit(llxx_monitorupdate())
    
