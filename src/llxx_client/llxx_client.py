# --*coding:utf-8*--
'''
Created on 2016年8月21日

@author: fanxin, eachen
'''

from abc import abstractmethod

import socket
import threading
class llxx_client_listner:
    
    '''
    receive message from service
    '''
    @abstractmethod
    def onMessage(self, message):pass
        


class llxx_client:
    def __init__(self, listenerApkService , listenerMonkeyRunnerService):
        
        # 监听客户端的点击事件
        self.socket_listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # 处理monkeyrunner的点击事件
        self.socket_monkeyrunner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        self.listener_apk_service = listenerApkService
        
        self.listener_monkeyrunner_service = listenerMonkeyRunnerService
        

    def _listener(self):
        print "_listener start"
        while(True):
            data = self.socket_listener.recv(1024 * 20)  # 阻塞线程，接受消息
            #print "_listener receive->" + data
            self.listener_apk_service(data)
        
    def _monkeyrunner(self):
        print "_monkeyrunner start"
        while(True):
            data = self.socket_monkeyrunner.recv(1024 * 20)  # 阻塞线程，接受消息
            #print "_listener receive->" + data
            self.listener_monkeyrunner_service(data)
            
    '''
    send message to Android Apk Service
    '''
    def sendToService(self, msg):
        self.socket_listener.sendall(msg)
        
    '''
    send message to MonkeyRunner Service
    '''
    def sendToMonkeyRunner(self, msg):
        self.socket_monkeyrunner.send(msg);
        
    def _start(self):
        try:
            # 调用connect 连接本地(127.0.0.1) 的8082端口
            self.socket_listener.connect(("127.0.0.1", 8082))
            # 开始连接
            t = threading.Thread(target=self._listener, args=())
            t.setDaemon(True)
            t.start()
        except:
            print "can`t connect 127.0.0.1:8082"
            
        try:
            # 调用connect 连接本地(127.0.0.1) 的9999端口
            self.socket_monkeyrunner.connect(("127.0.0.1", 9999))
            # 开始连接
            t = threading.Thread(target=self._monkeyrunner, args=())
            t.setDaemon(True)
            t.start()
        except:
            print "can`t connect 127.0.0.1:9999"
