# --*coding:utf-8*--
'''
Created on 2016年9月13日

@author: fanxin, eachen
@summary: 封装测试单元
'''
class PlugUnit:
    """ 定义一个接口，其他 插件必须实现这个接口，name 属性必须赋值 """
    name = ''
    description = ''
    version = ''
    
    needReStart = False
    def __init__(self):
        pass
    
    def run(self):
        print "startTest"
    
    '''
    @note: 获取插件的描述
    '''
    def getDescription(self):
        return self.description
    
    '''
    @note: 获取插件的名字
    '''
    def getName(self):
        return self.name
    
    '''
    @note: 获取版本信息
    '''
    def getVersion(self):
        return self.version
    
    '''
    @note: 是否需要因为监视器重新启动
    '''
    def setReStartByMonitor(self, isReStart):
        self.needReStart = isReStart
        