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
        
        self.uiautomator_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # 处理monkeyrunner的点击事件
        self.socket_monkeyrunner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        self.listener_apk_service = listenerApkService
        
        self.listener_monkeyrunner_service = listenerMonkeyRunnerService
        
    def _setuiautomator_listtener(self, uiautomator_listtener):
        self.uiautomator_listtener = uiautomator_listtener
        
    def _listener(self):
        print "_listener start"
        
        # BUG 这里的分段1057 需要严格测试
        dataAll = ""
        while(True):
            data = self.socket_listener.recv(1024)  # 阻塞线程，接受消息
            dataAll = dataAll + data
            if(data.__sizeof__() != 1057):
                #print "_listener receive->" + data
                self.listener_apk_service(dataAll)
                dataAll = ""
        
    def _monkeyrunner(self):
        print "_monkeyrunner start"
        dataAll = ""
        while(True):
            data = self.socket_monkeyrunner.recv(1024)  # 阻塞线程，接受消息
            #print "_listener receive->" + data
            dataAll = dataAll + data
            if(data.__sizeof__() != 1057):
                #print "_listener receive->" + data
                self.listener_monkeyrunner_service(dataAll)
                dataAll = ""
    def _uiautomator(self):
        print "_uiautomator start"
        dataAll = ""
        while(True):
            data = self.uiautomator_client.recv(1024)  # 阻塞线程，接受消息
            #print "_listener receive->" + data
            dataAll = dataAll + data
            if(data.__sizeof__() != 1057):
                #print "_listener receive->" + data
                if self.uiautomator_listtener != None and dataAll != '':
                    self.uiautomator_listtener(dataAll)
                    dataAll = ""       
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
        
    
    def sendToUiAnimator(self, msg):
        self.uiautomator_client.send(msg)
        
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
            # 调用connect 连接本地(127.0.0.1) 的8082端口
            self.uiautomator_client.connect(("127.0.0.1", 8083))
            # 开始连接
            t = threading.Thread(target=self._uiautomator, args=())
            t.setDaemon(True)
            t.start()
        except:
            print "can`t connect 127.0.0.1:8083"
            
        try:
            # 调用connect 连接本地(127.0.0.1) 的9999端口
            self.socket_monkeyrunner.connect(("127.0.0.1", 9999))
            # 开始连接
            t = threading.Thread(target=self._monkeyrunner, args=())
            t.setDaemon(True)
            t.start()
        except:
            print "can`t connect 127.0.0.1:9999"
