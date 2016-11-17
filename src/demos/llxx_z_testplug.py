# --*coding:utf-8*--
'''
Created on 2016年11月17日

@author: fanxin, eachen
'''

from llxx_app import llxx_app
from llxx_command import UiSelectAction
from llxx_plugunit import PlugUnit

app = llxx_app("com.llxx.service")

app.startActivity("com.llxx.socket.MainActivity")


__all__ = ["PlugTestListview"]
class PlugTestListview(PlugUnit):
    
    def __init__(self):
        self.name = "testlistview"
        self.version = 1.0
        self.description = "test list view scoller and click"
        
    def run(self):
        UiSelectAction().text("Toast_").performClick()

app.addTestUnit(PlugTestListview())
app.start()
