# --*coding:utf-8*--
'''
Created on 2016年11月19日

@author: fanxin, eachen
使用监视器组件来辅助测试
'''

from llxx_app import llxx_app
from monitor.monitor_startactivity import MonitorStartActivity
from monitor.monitor_click import MonitorClick
from monitor.monitor_window_state import MonitorWindowState
from monitor.monitor_dialog import MonitorDialog
from time import sleep

app = llxx_app("com.llxx.service")

# # 监听意外弹出框
app.addMonitorUnit(MonitorWindowState())
app.addMonitorUnit(MonitorStartActivity())
app.addMonitorUnit(MonitorClick())
app.addMonitorUnit(MonitorDialog())

sleep(10000)
app.start()