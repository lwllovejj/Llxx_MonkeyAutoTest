# --*coding:utf-8*--
'''
Created on 2016年8月29日

@author: fanxin, eachen
'''

from llxx_command import QueryCommand


from llxx_client_wrap import llxx_client_wrap
import simplejson as json
import time

client = llxx_client_wrap()
testuinode = {}

queryId = QueryCommand()
    
nodes = queryId.queryHierarchy()

testuinode["action"] = "test-uinode"
params = {}
testuinode["params"] = params
params["node"] = nodes

print json.dumps(testuinode, sort_keys=True)
client.sendToUianimator(json.dumps(testuinode, sort_keys=True) + "}")

while True:
    
    time.sleep(2)