# --*coding:utf-8*--
'''
Created on 2016年10月27日

@author: fanxin, eachen
@summary: Contxt，为当前测试提供上下文环境
'''

from llxx_command import Query

class llxx_app_context:
    
    def __init__(self, client, package):
        self._client = client
        self._package = package
        
    def allActivity(self):
        query_ = Query()
        return query_.getAllActivity(self._package)
    
if __name__ == '__main__':
    pass