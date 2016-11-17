# --*coding:utf-8*--
'''
Created on 2016年11月17日

@author: fanxin, eachen
@note: 
'''
import llxx_app
import threading


class llxx_command_control():
    
    passArray = {}
    def __init__(self):
        self._ispass = False
        pass
    
    '''
    @note: 执行命令
    '''
    def setPass(self, name, isPass):
        self.passArray[name] = isPass
        return self
    
    '''
    @note: 是否不执行命令
    '''
    def isPass(self, name):
        return self.passArray[name]
    
def getCommandControl():
    return llxx_app.llxx_app._llxx_command_control

'''
是否停止执行命令
'''
def isCommandPass():
    thread = threading.current_thread()
    return getCommandControl().isPass(thread.getName())

