#--*coding:utf-8*--

import os
import threading


class StartMonkeyService(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)


    def run(self):
        print ('StartMonkeyService...')
        cmd = 'monkeyrunner ' + os.getcwd()
        cmd = cmd + '\\services\\MokeyGetBItmapService.py'
        print ("run command : " + cmd)
        os.system(cmd)
        print ('be there')