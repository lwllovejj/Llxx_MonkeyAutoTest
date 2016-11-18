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

def sendMessageToApp(reportMessage):
    getReportListener().sendMessage(reportMessage)
    
# 测试状态
REPORT_MSG_TYPE_TEST_STATUS = 1

# 进入监控
REPORT_MSG_TYPE_IN_MONITOR = 2

# 退出监控
REPORT_MSG_TYPE_OUT_MONITOR = 3

'''
上报信息
'''
class reportMessage():
    
    
    def __init__(self):
        self.sucess = False
        self.type = REPORT_MSG_TYPE_TEST_STATUS
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
    
    '''
    @note: 设置上报消息类型
    '''
    def setType(self, msg_type):
        self.type = type
        return self
    
    '''
    @note: 获取上报消息类型
    '''
    def getType(self):
        return self.type
        