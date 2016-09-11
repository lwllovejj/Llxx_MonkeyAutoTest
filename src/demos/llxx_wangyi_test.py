# --*coding:utf-8*--
'''
Created on 2016年8月26日

@author: fanxin, eachen
'''
import os

from llxx_client_wrap import llxx_client_wrap
from llxx_command import ClickCommand
from llxx_wait import llxx_wait
from llxx_command import RegPakcages
from llxx_command import TakeSnapshot

client = llxx_client_wrap()

regpackages = RegPakcages(client)
package = []
package.append("com.netease.newsreader.activity")
print regpackages.regPackages(package)

print "------------"

package = "com.netease.newsreader.activity"

os.system("adb shell am force-stop com.netease.newsreader.activity")
os.system("adb shell am start com.netease.newsreader.activity/com.netease.nr.biz.ad.AdActivity")
 
# com.netease.newsreader.activity/com.netease.nr.phone.main.MainActivity
# 等待主Activity启动

print "等待主Activity启动: " + str(llxx_wait(client).waitForActivity("com.netease.nr.phone.main.MainActivity"))

#点击 娱乐标签 
print "点击 娱乐标签 : " + str(ClickCommand(client).performClickByNameIndex("娱乐", 0))

llxx_wait(client).waitForTime(3)

takeSnapshot = TakeSnapshot(client)
currendir = os.getcwd()
print takeSnapshot.takeSnapshot(currendir + "//snapshot_yule.png")
