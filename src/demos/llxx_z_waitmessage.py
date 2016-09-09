# --*coding:utf-8*--
'''
Created on 2016年9月9日

@author: fanxin, eachen
'''

import time
## 测试接收服务端的各种
from llxx_client_wrap import llxx_client_wrap


class llxx_wait_message:
    
    messageList = [] 
    def __init__(self, llxx_client_wrap):
        self._llxx_client_wrap = llxx_client_wrap
        self._llxx_client_wrap.regMessageListner(self)
    
    def onMessage(self, message):
        if message.strip() != "":
            self.messageList.append(message)
            print "llxx_wait_message onMessage ->" + message
        
client = llxx_client_wrap()
wait = llxx_wait_message(client)

while(True):
    time.sleep(1)

