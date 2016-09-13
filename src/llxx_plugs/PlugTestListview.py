# --*coding:utf-8*--
'''
Created on 2016年9月14日

@author: fanxin, eachen
'''
from llxx_plugunit import PlugUnit
__all__ = ["PlugTestListview"]
class PlugTestListview(PlugUnit):
    
    def __init__(self):
        self.name = "testlistview"
        self.version = 1.0
        self.description = "test list view scoller and click"
    
    def run(self, llxx_client):
        print "test list view"