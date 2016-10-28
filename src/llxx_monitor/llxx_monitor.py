# --*coding:utf-8*--
'''
Created on 2016年10月28日

@author: fanxin, eachen
'''
# pip install simplejson
from llxx_client_wrap import llxx_client_wrap
import time

import threading

class llxx_monitor:
    
    messageList = [] 
    monitorunits = []
    def __init__(self, llxx_client_wrap):
        self._llxx_client_wrap = llxx_client_wrap
        self._start = True
        self._debug = False
        
        # 开始连接
        t = threading.Thread(target=self.monitor, args=())
        t.setDaemon(False)
        t.start()
    
    def onMessage(self, message):
        if message.strip() != "":
            self.messageList.append(message)
        # print "llxx_wait onMessage ->" + message
    
        # # 等待指定的数据
    '''
    @param maps: 对应数据字典
    @param timeout: 超时时间
    '''
    def monitor(self):
        self._llxx_client_wrap.regMessageListner(self)
        message = None
        while self._start:
            pass_message = []
            for msg in self.messageList:
                for monitor_unit in self.monitorunits:
                    try:
                        monitor_unit.onMonitor(msg)
                        pass_message.append(msg)
                        if self._debug:
                            print msg
                    except Exception,ex:
                        print Exception,":",ex

            # print 'time pass' + str(timetotal)
            for msg in pass_message:
                self.messageList.remove(msg)
                
            time.sleep(0.2)
        self._llxx_client_wrap.unRegMessageListener(self)
        return message
    
    '''
    add monitor unit
    '''
    def addMonitorUnit(self, unit):
        self.monitorunits.append(unit)
    
    '''
    remote monitor unit
    '''
    def removeMonitoUnit(self, unit):
        self.monitorunits.remove(unit)

    def start(self):
        self._start = True
        
    def stop(self):
        self._start = False
        
    def setDebug(self, debug):
        self._debug = debug
        
class llxx_monitorunit:  
    
    def onMonitor(self, message):
        pass
    
if __name__ == '__main__':
    monitor = llxx_monitor(llxx_client_wrap())
    
