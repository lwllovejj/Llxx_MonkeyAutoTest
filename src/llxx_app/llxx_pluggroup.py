# --*coding:utf-8*--
'''
Created on 2016年9月13日

@author: fanxin, eachen
@summary: 封装测试组，这里代表了一组测试
'''

class PlugGroup:
    llxx_testunits = []
    def __init__(self, llxx_client):
        self._client_wrap = llxx_client
    
    def addTestUnits(self, unit):
        self.llxx_testunits.append(unit)
    
    def run(self):
        for unit in self.llxx_testunits:
            unit.run(self._client_wrap)