# --*coding:utf-8*--
'''
Created on 2016年10月20日

@author: fanxin, eachen

搜集点击跳转
'''
# pip install simplejson
import string

from llxx_monitor import llxx_monitorunit, llxx_result


class llxx_monitor_clickcollect(llxx_monitorunit):  
    
    def onMonitor(self, message):
        isInstall = string.find(message, "start_activity") != -1
        if isInstall:
            params = {};
            self.hookApp(llxx_result(message, "ui_update", params))
            print message
        
        ## 安装完成
        isInstallOk = string.find(message, "start_dialog") != -1
        if isInstallOk:
            params = {};
            self.hookApp(llxx_result(message, "ui_update", params))
            print message
            
