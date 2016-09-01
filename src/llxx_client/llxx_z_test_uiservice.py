# --*coding:utf-8*--
'''
Created on 2016年8月29日

@author: fanxin, eachen
'''

from llxx_command import QueryCommand


from llxx_client_wrap import llxx_client_wrap
import simplejson as json
from llxx_wait import llxx_wait
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
client.sendToUianimator(json.dumps(testuinode, sort_keys=True))
print llxx_wait("",client).waitFor(testuinode, 10)

