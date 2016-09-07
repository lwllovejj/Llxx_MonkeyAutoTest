# --*coding:utf-8*--
'''
Created on 2016年9月7日

@author: fanxin, eachen
'''

from llxx_command import RegPakcages

## 注册测试
from llxx_client_wrap import llxx_client_wrap

client = llxx_client_wrap()
regpackages = RegPakcages(client)
package = []
package.append("com.baidu.BaiduMap")
package.append("com.android.settings")
print regpackages.regPackages(package)
