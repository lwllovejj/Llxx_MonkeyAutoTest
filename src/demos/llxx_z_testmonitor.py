# --*coding:utf-8*--
'''
Created on 2016年11月28日

@author: fanxin, eachen
'''

from llxx_app import llxx_app
from llxx_z_testunit_uiselect import PlugTestUiSelect
from llxx_z_testunit_monitor import TestMonitor

app = llxx_app("com.llxx.service")

app.addMonitorUnit(TestMonitor())

app.addTestUnit(PlugTestUiSelect(app))
app.start()
