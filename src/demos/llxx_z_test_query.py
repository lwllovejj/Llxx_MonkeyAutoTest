# --*coding:utf-8*--
'''
Created on 2016年8月27日

@author: fanxin, eachen
'''

from llxx_command import QueryCommand

#queryNome = QueryCommand()
#print queryNome.queryListView()


queryId = QueryCommand()
# lists = queryId.queryIdNotNull()
# for node in lists:
#     print node
    
lists = queryId.queryCanclick()
for node in lists:
    print node