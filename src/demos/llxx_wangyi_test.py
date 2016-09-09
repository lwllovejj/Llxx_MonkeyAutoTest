# --*coding:utf-8*--
'''
Created on 2016年8月26日

@author: fanxin, eachen
'''
import os

from llxx_client_wrap import llxx_client_wrap
from llxx_command import ClickCommand
from llxx_command import QueryCommand
from llxx_wait import llxx_wait
from llxx_command import RegPakcages

client = llxx_client_wrap()

regpackages = RegPakcages(client)
package = []
package.append("com.netease.newsreader.activity")
print regpackages.regPackages(package)

print "------------"
click = ClickCommand()

package = "com.netease.newsreader.activity"

os.system("adb shell am force-stop com.netease.newsreader.activity")
os.system("adb shell am start com.netease.newsreader.activity/com.netease.nr.biz.ad.AdActivity")
 
# com.netease.newsreader.activity/com.netease.nr.phone.main.MainActivity
# 等待主Activity启动
waitActivity = llxx_wait(client);
isMatch = waitActivity.waitForActivity("com.netease.nr.phone.main.MainActivity")
if isMatch:
    print "waitForActivity com.netease.nr.phone.main.MainActivity ok"
