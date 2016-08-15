# --*coding:utf-8*--
'''
Created on 2016年7月27日

@author: Administrator
'''

import wx

import os

import sys 
import socket
import threading, time

from services  import StartMonkeyService
class MyFrame(wx.Frame):
        def __init__(self):
            wx.Frame.__init__(self, None, -1, size=(1280, 720), title="自动测试工具".decode('utf-8', 'ignore'))  # "2016/7/27 星期三".decode('utf-8','ignore'))
            self.panel = MyPanel(self)
            
class MyPanel(wx.Panel):
        
        global data
        global clien_socket;
        data = []
        def __init__(self, Parent):                      
            wx.Panel.__init__(self, Parent, -1)
            
            print os.getcwd() 
            self.pic = wx.Button(self, -1, pos=(500, 100), size=(100, 50), label="11")
            self.pic.Bind(wx.EVT_BUTTON, self.onGetPic)
            
            # # 添加一张图片显示在x=30，y=50的位置
            self.myImage = wx.StaticBitmap(self, -1, pos=(10, 10), size=(240, 400))
            
            monkeyServer = StartMonkeyService.StartMonkeyService()
            monkeyServer.start()
            print "MonkeyService is start()"
            
            time.sleep(2)
            self.connectService()
            
        # # 处理接收消息
        def recieve_msg(self, username, skt):
            print 'receive_msg'
            global isNormar, other_usr
            
            # # 发送用户登录信息，服务端会对应解析
            skt.send('login|%s' % username)
            while(True):
                data = skt.recv(1024)  # 阻塞线程，接受消息
                msg = data.split('|')
                if msg[0] == 'login':
                    print u'%s user has already logged in, start to chat' % msg[1]
                    other_usr = msg[1]
                if msg[0] == 'tackPic':
                    # #print u'tackPic status %s' % msg[1]
                    if msg[1] == 'finsh':
                        print u'tackPic path %s' % msg[2]
                        # bmp=wx.Bitmap(msg[2], wx.BITMAP_TYPE_PNG) 
                        # self.myImage.SetBitmap(bmp)
                        img = wx.Image(msg[2], wx.wx.BITMAP_TYPE_PNG)
                        w = img.GetWidth()
                        h = img.GetHeight()
                        # img = img.Rescale(w/2,h/2)
                        img.Rescale(w / 2, h / 2)
                        self.myImage.SetBitmap(img.ConvertToBitmap())
                    
                else:
                    print msg[0]

        def connectService(self):
            
            global isNormar, other_usr  
            try:
                usrname = 'xingxing'
                # 创建一个套接字
                self.clien_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                
                # 调用connect 连接本地(127.0.0.1) 的9999端口
                self.clien_socket.connect(("127.0.0.1", 9999))
                
                # 开始连接
                t = threading.Thread(target=self.recieve_msg, args=(usrname, self.clien_socket))
                t.start()
            except:
                print 'connection exception'
                # self.connectService()
                isNormar = False
            finally:
                pass

        def onGetPic(self, event):
            monkeyServer = StartMonkeyService.StartMonkeyService()
            monkeyServer.start()
        
class MyApp(wx.App):
        def OnPreInit(self, *args, **kwargs):
            frame = MyFrame()
            frame.Show()
            self.MainLoop()
            return wx.App.OnPreInit(self, *args, **kwargs)
if __name__ == "__main__":
        app = MyApp()
