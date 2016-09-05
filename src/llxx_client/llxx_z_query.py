# --*coding:utf-8*--
'''
Created on 2016年8月29日

@author: fanxin, eachen
'''

from llxx_command import Query


from llxx_client_wrap import llxx_client_wrap

client = llxx_client_wrap()
query = Query(client)
query.getTopActivity()
