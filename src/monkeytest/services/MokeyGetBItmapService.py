# --*coding:utf-8*--
import os
import time

# 导入线程socket需要的模块
import sys 
import socket
import threading, time

# 导入MonkeyRunner 并且命名别名为mr
from com.android.monkeyrunner import MonkeyRunner as mr
from com.android.monkeyrunner import MonkeyDevice as md
from com.android.monkeyrunner import MonkeyImage as mi
from __builtin__ import file

# 用户对象
class client:
    ## 创建一个用户，传入对方连接的套接字接口和用户名
    def __init__(self, skt, username='none'):
        self.skt=skt
        self.username=username
        
    # 发送消息
    def send_msg(self,msg):
        self.skt.send(msg)
        
    # 退出登录
    def logout(self):
        self.skt.close()


# # 客户端列表
clienList = [] 
class MonkeyGetBitmapService(threading.Thread):
    def __init__(self):
        
        ### 
        print("start service socket")
        ## 开启服务端线程
        ll_socket_service = threading.Thread(target=self.startSocket, args=());
        
        # 开始运行线程，当这里调用开始之后就会执行hand_user_con
        ll_socket_service.start()  
        
        
        print ("waitForConnection...")
        # 在导入的时候MonkeyRunner 被命名为了mr,这里开始等待手机的连接
        self.device = mr.waitForConnection()
        
        # 唤醒手机屏幕，如果屏幕么有唤醒是无法获取build.model 的
        self.device.wake();
        # 获取手机的build.model 
        name = self.device.getProperty('ro.product.model')
    
        # print (name)
        print "%s Phone has connect by adb ..." % (name)
        self.path = 'D:\\screenshot\\'
        self.filename = 'monkeyPic'
        
    def hand_user_con(self, user):
        ## print "hand_user_con %s" % (user.username)
        print "hand_user_con"
#         try:
#             isNormar=True
#             while isNormar:
#                 print("hand_user_con wait for data...")
#                 data=user.skt.recv(1024)
#                 time.sleep(1)
#                 #分析消息
#                 msg=data.split('|')
#                 
#                 ## 登录消息，记录名字
#                 if msg[0]=='login':
#                     print 'user [%s] login' % msg[1]
#                     user.username=msg[1]
#         except:
#             isNormar=False
    
    def send_msg(self, msg):
        ## 给指定用户名的人发送消息
        for usr in clienList:
            usr.skt.send(msg)
                
    def startSocket(self):
        # 创建一个套接字
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 监听本地(0.0.0.0) 的 9999端口
        s.bind(('0.0.0.0', 9999))
        
        # 设置最多监听5个用户？
        s.listen(5)
        
        while True:
            print u'waiting for client connection...'
            # 等待用户连接，程序会在这里阻塞，当有用户连接到这里的时候，就会执行下面的流程
            sock, addr = s.accept()
            
            # 接收到用户连接，返回连接成功的Socket，创建一个用户
            user = client(sock)
            
            # 将当前用户添加到用户列表(userlist) 中
            clienList.append(user)
            
            # 开启一个线程处理用户连接,target=hand_user_con 的意思是，在调用线程的start方法后执行hand_user_con，args里面传的是
            # hand_user_con 这个方法需要传递的参数
            t = threading.Thread(target=self.hand_user_con, args=(user,));
            
            # 开始运行线程，当这里调用开始之后就会执行hand_user_con
            t.start()  
        s.close()
    
    
    def run(self):
        self.ctrl = 1
        while self.ctrl == 1:
            
            # file = open('D:\\screenshot\\ctrl.txt','w')
            # file.write('0')
#             print '0'
            # file.close()
            
            # # 使用 MonkeyDevice 截取图片，并且保存到D盘的screenshot 文件夹
            ## print ('start takeSnapshot')
            
            ## 发送  tackPic|start 到所有连接到这里的客户端，通知客户端截图开始了
            self.send_msg("tackPic|start")
            filepath = self.path + self.filename + '.png';
            ## print(filepath)
            result = self.device.takeSnapshot()
            result.writeToFile (filepath, 'png')
            
            ## 发送"tackPic|finsh|" + filepath 到所有的连接到这里的客户端，通知客户端截图结束以及截图的位置
            ## 接收消息参看monkeyrunner_demo.py 里面的recieve_msg(self, username, skt):方法，这里
            ## 解析了这个参数，获取文件的路径并且做了显示
            self.send_msg("tackPic|finsh|" + filepath)
            ## print ('end takeSnapshot')
            
            # # 使用socket通讯，不使用文件写入0或者1来标志是否截图成功
            # file = open('D:\\screenshot\\ctrl.txt','w')
            # file.write('1')
            # file.close()
#             print '1'
#             print 'thread is running'
            #time.sleep(0.2)
            
MonkeyGetBitmapService().run()
