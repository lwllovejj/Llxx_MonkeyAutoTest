# --*coding:utf-8*--
'''
Created on 2016年8月21日

@author: fanxin, eachen
'''

import socket
import threading

class llxx_client:
    def __init__(self):
        
        # 监听客户端的点击事件
        self.socket_listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # 处理monkeyrunner的点击事件
        self.socket_monkeyrunner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        

    def _listener(self):
        print "_listener start"
        while(True):
            data = self.socket_listener.recv(1024 * 20)  # 阻塞线程，接受消息
            print "_listener receive->" + data
        
    def _monkeyrunner(self):
        print "_monkeyrunner start"
        while(True):
            data = self.socket_monkeyrunner.recv(1024 * 20)  # 阻塞线程，接受消息
            print "_listener receive->" + data
        
    def _start(self):
        try:
            # 调用connect 连接本地(127.0.0.1) 的8082端口
            self.socket_listener.connect(("127.0.0.1", 8082))
            # 开始连接
            t = threading.Thread(target=self._listener, args=())
            t.start()
        except:
            print "can`t connect 127.0.0.1:8082"
            
        try:
            # 调用connect 连接本地(127.0.0.1) 的9999端口
            self.socket_monkeyrunner.connect(("127.0.0.1", 9999))
            # 开始连接
            t = threading.Thread(target=self._monkeyrunner, args=())
            t.start()
        except:
            print "can`t connect 127.0.0.1:9999"

llxx_client = llxx_client();
llxx_client._start()