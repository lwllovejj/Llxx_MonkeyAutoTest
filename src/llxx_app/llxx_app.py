# --*coding:utf-8*--
'''
Created on 2016年9月12日

@author: fanxin, eachen
@summary: 封装单 APP 测试
'''

from llxx_client_wrap import llxx_client_wrap
from llxx_setuperror import Llxx_SetupError
from llxx_command import RegPakcages

class llxx_app:
    
    def __init__(self, package):
        self._client = llxx_client_wrap()
        self._regapp = False
        
        ### 添加需要测试的package
        regpackages = RegPakcages(self._client)
        packages = []
        packages.append(package)
        self._regapp = regpackages.regPackages(packages)
        if self._regapp:
            print "init test package : " + package + " ok !!!"
        else:
            raise Llxx_SetupError("reg test package error")
    
    
if __name__ == '__main__':
    pass