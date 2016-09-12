# --*coding:utf-8*--
'''
Created on 2016年9月12日

@author: fanxin, eachen
'''
class Llxx_SetupError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)