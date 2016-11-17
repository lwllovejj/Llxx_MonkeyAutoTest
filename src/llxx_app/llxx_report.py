# --*coding:utf-8*--
'''
Created on 2016年11月17日

@author: fanxin, eachen
@note: 
'''
import llxx_app
def getReportListener():
    return llxx_app.llxx_app._llxx_report_listener

def reportError(errorReason):
    getReportListener().onReportError(errorReason)
    
def reportSucess(sucessDes):
    getReportListener().onReportSucess(sucessDes)
    
'''
上报信息
'''
class reportMessage():
    
    
    def __init__(self):
        self.sucess = False
        self.msg = ""
    
    '''
    @note: 设置是否执行成功
    '''
    def setSucess(self, sucess):
        self.sucess = sucess
        return self
    
    '''
    @note: 是否执行成功
    '''
    def isSucess(self):
        return self.sucess
    
    '''
    @note: 设置当前汇报的消息内容
    '''
    def setMessage(self, message):
        self.msg = message
        return self;
    
    '''
    @note: 获取当前执行的消息
    '''
    def getMessage(self):
        return self.msg
        