# --*coding:utf-8*--
'''
Created on 2016年9月12日

@author: fanxin, eachen
@summary: 封装单 APP 测试
'''

from llxx_client_wrap import llxx_client_wrap
from llxx_setuperror import Llxx_SetupError
from llxx_command import RegPakcages
from llxx_pluggroup import PlugGroup

class llxx_app:
    
    _pluggroups = []
    def __init__(self, package):
        self._client = llxx_client_wrap()
        self._regapp = False
        
        self._defgroup = PlugGroup(self._client)
        self._pluggroups.append(self._defgroup)
        ### 添加需要测试的package
        regpackages = RegPakcages(self._client)
        packages = []
        packages.append(package)
        self._regapp = regpackages.regPackages(packages)
        if self._regapp:
            print "init test package : " + package + " ok !!!"
        else:
            raise Llxx_SetupError("reg test package error")
    
    '''
    add test group
    '''
    def addTestGroup(self, group):
        self._pluggroups.append(group)
    
    '''
    add test units to def group
    '''
    def addTestUnits(self, unit):
        self._defgroup.addTestUnits(unit)
    
    def addTestPlugs(self, name):
        self._defgroup.addTestPlugs(name)
    
    '''
    
    '''
    def run(self):
        for group in self._pluggroups:
            group.run()
if __name__ == '__main__':
    pass