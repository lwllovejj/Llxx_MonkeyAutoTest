# --*coding:utf-8*--
'''
Created on 2016年10月27日

@author: fanxin, eachen
@summary: Contxt，为当前测试提供上下文环境
'''

from llxx_client_wrap import llxx_client_wrap
from llxx_command import Query
from llxx_command import QueryCommand

class llxx_app_context:
    
    def __init__(self, client, package):
        self._client = client
        self._package = package
        
    def allActivity(self):
        query_ = Query(self._client)
        return query_.getAllActivity(self._package)
    
if __name__ == '__main__':
    pass