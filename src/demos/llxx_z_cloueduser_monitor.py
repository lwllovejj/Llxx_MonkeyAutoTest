# --*coding:utf-8*--
'''
Created on 2016年10月29日

@author: fanxin, eachen

APP自己调用安装
'''
# pip install simplejson
import string

from llxx_monitor import llxx_monitorunit, llxx_result

class llxx_monitor_dialog(llxx_monitorunit):  
    
    #
    def getTimeOut(self):
        return 120
    
    def onMonitor(self, message):
        isShow = string.find(message, "start_dialog") != -1 and string.find(message, "知道了") != -1
        if isShow:
            # print message
            params = {};
            self.hookApp(llxx_result(message, "llxx_monitor_dialog", params))
            #self.remove()
            # print message
            
