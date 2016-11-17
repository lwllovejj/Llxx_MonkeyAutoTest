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
    def __init__(self):
        pass
    
    def run(self):
        print "startTest"
        
    def getDescription(self):
        return self.description
    
    def getName(self):
        return self.name
    
    def getVersion(self):
        return self.version