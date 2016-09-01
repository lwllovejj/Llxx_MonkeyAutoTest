# --*coding:utf-8*--
'''
Created on 2016年8月26日

@author: fanxin, eachen
'''
# pip install simplejson
import simplejson as json
import time

class llxx_wait:
    
    messageList = [] 
    def __init__(self, packagename, llxx_client_wrap):
        self._packagename = packagename
        self._llxx_client_wrap = llxx_client_wrap
    
    def onMessage(self, message):
        if message.strip() != "":
            self.messageList.append(message)
        # print "llxx_wait onMessage ->" + message
    
    ## 等待指定的数据
    '''
    @param maps: 对应数据字典
    @param timeout: 超时时间
    '''
    def waitFor(self, maps , timeout):
        self._llxx_client_wrap.regMessageListner(self)
        isMatch = False
        timetotal = 0.0
        message = None
        while True and (isMatch == False and timetotal < timeout):
            for msg in self.messageList:
                target = json.JSONDecoder().decode(msg)
                isMatch = True
                # 遍历数组中的元素
                for key in maps.keys():
                    if key == 'params':
                        continue
                    
                    if target[key] != maps[key]:
                        isMatch = False
                        
                if isMatch:
                    message = target
                    self.messageList.remove(msg)
                    break;
            # print 'time pass' + str(timetotal)
            timetotal += 0.1
            time.sleep(0.1)
        self._llxx_client_wrap.unRegMessageListener(self)
        if message != None:
            return message["sucess"]
        print "wait for " + str(maps) + " timeout"
        return False
        
    
    def waitForActivity(self, activityName):
        self._llxx_client_wrap.regMessageListner(self)
        isMatch = False
        isBreak = False
        while True and (isBreak == False):
            #print self.messageList
            for msg in self.messageList:
                target = json.JSONDecoder().decode(msg)
                if target['action'] == "start" and target['classname'] == activityName and target['type'] == "activity":
                    isMatch = True;
                    isBreak = True
                    self.messageList.remove(msg)
                    break;
                
        self._llxx_client_wrap.unRegMessageListener(self)
        return isMatch
    
    '''
    @return:  是否弹出了toast
    '''
    def waitForNotifyToast(self, title):
        return self.waitForNotifiToast("android.widget.Toast$TN", title)
    
    '''
    @return 是否弹出了指定toast
    '''
    def waitForNotifiToast(self, classname, title):
        self._llxx_client_wrap.regMessageListner(self)
        isMatch = False
        isBreak = False
        while True and (isBreak == False):
            #print self.messageList
            for msg in self.messageList:
                    target = json.JSONDecoder().decode(msg)
                    if target['action'] == "notify" and target['classname'] == classname and target['title'] == title:
                        isMatch = True
                        isBreak = True
                        self.messageList.remove(msg)
                        break;
        self._llxx_client_wrap.unRegMessageListener(self)
        
        return isMatch

    def waitForClick(self, classname , title):
        self._llxx_client_wrap.regMessageListner(self)
        isMatch = False
        isBreak = False
        while True and (isBreak == False):
            #print self.messageList
            for msg in self.messageList:
                target = json.JSONDecoder().decode(msg)
                if target['action'] == "click" and target['classname'] == classname and target['title'] == title:
                    isMatch = True
                    isBreak = True
                    self.messageList.remove(msg)
                    break;
                
        self._llxx_client_wrap.unRegMessageListener(self)
        return isMatch
