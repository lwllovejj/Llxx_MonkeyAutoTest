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

os.system("adb forward tcp:8082 tcp:8082")
    
client = llxx_client_wrap()
print "------------"
click = ClickCommand()

package = "com.netease.newsreader.activity"

os.system("adb shell am force-stop com.netease.newsreader.activity")
os.system("adb shell am start com.netease.newsreader.activity/com.netease.nr.biz.ad.AdActivity")
 
# com.netease.newsreader.activity/com.netease.nr.phone.main.MainActivity
waitActivity = llxx_wait("com.netease.newsreader.activity", client);
isMatch = waitActivity.waitForActivity("com.netease.nr.phone.main.MainActivity")
if isMatch:
    print "waitForActivity com.netease.nr.phone.main.MainActivity ok"


queryNome = QueryCommand()
queryNome.queryListView()
client.runCommand(queryNome)
print queryNome.getCommand()

##　test perform click text
# click.performClickByName(u"军事")
waitForClick = llxx_wait(u"com.llxx.service", client);
# client.runCommand(click)
# isMatch = waitForClick.waitForClick(u"android.widget.TextView", u"军事")
# if isMatch:
#     print "waitForClick ok"
#     

queryNome.queryListView()
client.runCommand(queryNome)
print queryNome.getCommand()

isMatch = waitForClick.waitForClick(u"android.widget.TextView", u"军事")
exit(0)
