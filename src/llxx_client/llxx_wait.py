# --*coding:utf-8*--
'''
Created on 2016年8月26日

@author: fanxin, eachen
'''
# pip install simplejson
import simplejson as json

class llxx_wait:
    
    messageList = [] 
    def __init__(self, packagename, llxx_client_wrap):
        self._packagename = packagename
        self._llxx_client_wrap = llxx_client_wrap
    
    def onMessage(self, message):
        self.messageList.append(message)
        print "llxx_wait onMessage ->" + message
         
    def waitForActivity(self, activityName):
        self._llxx_client_wrap.regMessageListner(self)
        while True:
            #print self.messageList
            if self.messageList.__len__() == 1:
                print self.messageList[0]
                break;
        self._llxx_client_wrap.unRegMessageListener(self)
    
    '''
    @return:  是否弹出了这个对话框
    '''
    def waitForNotifyToast(self, title):
        self._llxx_client_wrap.regMessageListner(self)
        isMatch = False
        isBreak = False
        while True and (isBreak == False):
            #print self.messageList
            for msg in self.messageList:
                target = json.JSONDecoder().decode(msg)
                if target['action'] == "notify" and target['classname'] == "android.widget.Toast$TN" and target['title'] == title:
                    isMatch = True;
                    isBreak = True
                    break;
        self._llxx_client_wrap.unRegMessageListener(self)
        
        return isMatch