# --*coding:utf-8*--
'''
Created on 2016年10月28日

@author: fanxin, eachen
'''
# pip install simplejson
from llxx_monitor import llxx_monitorunit, llxx_result
from llxx_monitor import llxx_monitor

import string


class llxx_monitorupdate(llxx_monitorunit):  
    
    def onMonitor(self, message):
        isHasUpate = string.find(message, "发现新版本，是否升级？") != -1 and string.find(message, "start_dialog") != -1
        if isHasUpate:
            print "发现新版本，是否升级？"
            params = [];
            self.hookApp(llxx_result(message, "update_dialog", params))
            # print message
        pass
    
if __name__ == '__main__':
    monitor = llxx_monitor()
    monitor.addMonitorUnit(llxx_monitorupdate())
    
