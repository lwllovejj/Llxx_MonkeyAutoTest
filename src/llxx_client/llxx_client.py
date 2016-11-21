# --*coding:utf-8*--
'''
Created on 2016年8月21日

@author: fanxin, eachen
'''

from abc import abstractmethod

#from __future__ import print_function
from websocket import create_connection

import socket
import threading
class llxx_client_listner:
    
    '''
    receive message from service
    '''
    @abstractmethod
    def onMessage(self, message):pass
        


class llxx_client:
    def __init__(self, listenerApkService):
        
        self.DEBUG = False
        # 监听客户端的点击事件
        
        self.listener_apk_service = listenerApkService
        self.socket_service_close = False
        self._debug_data_recv = False
        
    def _setuiautomator_listtener(self, uiautomator_listtener):
        self.uiautomator_listtener = uiautomator_listtener
        
    def _listener(self):
        print "_listener start"
        
        # BUG 这里的分段1057 需要严格测试
        while(True):
            try:
                data = self.socket_listener.recv()  # 阻塞线程，接受消息
                if self._debug_data_recv:
                    print data
                self.listener_apk_service(data)
            except Exception, e:
                if str(e).strip() == "[Errno 10053]":
                    self.socket_service_close = True
                    print "Error: socket_listener service is closed"
                    break;
                
    '''
    send message to Android Apk Service
    '''
    def sendToService(self, msg):
        try:
            self.socket_listener.send(msg)
        except:
            print "socket_listener not connect"
            if self.DEBUG:
                print msg
            return False
        return True
        
    
    def _start(self):
        try:
            # 调用connect 连接本地(127.0.0.1) 的8082端口
            self.socket_listener = create_connection("ws://127.0.0.1:8082/")
            # 开始连接
            t = threading.Thread(target=self._listener, args=())
            t.setDaemon(True)
            t.start()
        except:
            #print "can`t connect 127.0.0.1:8082"
            self.socket_service_close = True
