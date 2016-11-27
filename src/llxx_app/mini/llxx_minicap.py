# --*coding:utf-8*--
'''
Created on 2016年11月27日
@author: fanxin, eachen
@note: 
'''
import socket
import threading
import Queue
import struct
from __builtin__ import str
from PIL import Image
import io
from wx import BitmapFromImage

'''
Format      C Type          Python                  字节数
x           pad byte        no value                1
c           char            string of length 1      1
b           signed char     integer                 1
B           unsigned char   integer                 1
?           _Bool           bool                    1
h           short           integer                 2
H           unsigned        short    integer        2
i           int             integer                 4
I           unsigned        int    integer or long  4
l           long            integer                 4
L           unsigned long   long                    4
q           long long       long                    8
Q           unsigned long   long    long            8
f           float           float                   4
d           double          float                   8
s           char[]          string                  1
p           char[]          string                  1
P           void *          long

注1.q和Q只在机器支持64位操作系统
注2.每个格式前可以有一个数字，表示个数
注3.s格式表示一定长度的字符串，4s表示长度为4的字符串，但是p表示的是pascal字符串
注4.P用来转换一个指针，其长度和机器字长相关
注5.最后一个可以用来表示指针类型的，占4个字节

'''

HOST = 'localhost'
PORT = 1717
messageList = Queue.Queue()

def listener():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 定义socket类型，网络通信，TCP
    s.connect((HOST, PORT))  # 要连接的IP与端口
    
    parseGlobalHeader(s)
    while 1:
        img = imgGetFromDevice(s)
        messageList.put(img)
        print "image ----" 
#         img.save('foo' + str(i) + '.jpg', 'JPEG', quality=80)
#         i += 1;
        
def parseGlobalHeader(socket):
    data = socket.recv(24)
    vers = struct.unpack_from("B", data, 0)[0]
    print("VERSION =", vers)

    header_size = struct.unpack_from("B", data, 1)[0]
    print("H SIZE =", header_size)

    proc_pid = struct.unpack_from("I", data, 2)[0]
    print("PID =", proc_pid)

    x_real = struct.unpack_from("I", data, 6)[0]
    y_real = struct.unpack_from("I", data, 10)[0]
    print("Real display size: ", x_real, "x", y_real)

    x_virt = struct.unpack_from("I", data, 14)[0]
    y_virt = struct.unpack_from("I", data, 18)[0]
    print("Real display size: ", x_virt, "x", y_virt)

    disp_or = struct.unpack_from("B", data, 22)[0]
    print("ORIENTATION =", disp_or)
    qirks = struct.unpack_from("B", data, 23)[0]
    print("qirks =", qirks)
    
buf = io.BytesIO()
'''
-----------------------SCREEN PROCESSING
'''
def imgGetFromDevice(socket):
    data = socket.recv(4)
    frame_size = struct.unpack_from("I", data, 0)[0]

    
    buf.seek(0)
    len_read = 0
    while len_read < frame_size:
        data = socket.recv(4096)
        len_read += len(data)

        buf.write(data)
    buf.seek(0)

    img = Image.open(buf)
    return img
        

# 开始连接
t = threading.Thread(target=listener, args=())
t.setDaemon(False)
t.start()
    
import wx

def WxImageToWxBitmap( myWxImage ) :
    return myWxImage.ConvertToBitmap()


def WxBitmapToWxImage( myBitmap ) :
    return wx.ImageFromBitmap( myBitmap )

#-----

def PilImageToWxBitmap( myPilImage ) :
    return WxImageToWxBitmap( PilImageToWxImage( myPilImage ) )

def PilImageToWxImage( myPilImage ):
    myWxImage = wx.EmptyImage( myPilImage.size[0], myPilImage.size[1] )
    myWxImage.SetData( myPilImage.convert( 'RGB' ).tobytes() )
    return myWxImage

# Or, if you want to copy any alpha channel, too (available since wxPython 2.5)
# The source PIL image doesn't need to have alpha to use this routine.
# But, a PIL image with alpha is necessary to get a wx.Image with alpha.

def PilImageToWxImageA( myPilImage, copyAlpha=True ) :

    hasAlpha = myPilImage.mode[ -1 ] == 'A'
    if copyAlpha and hasAlpha :  # Make sure there is an alpha layer copy.

        myWxImage = wx.EmptyImage( *myPilImage.size )
        myPilImageCopyRGBA = myPilImage.copy()
        myPilImageCopyRGB = myPilImageCopyRGBA.convert( 'RGB' )    # RGBA --> RGB
        myPilImageRgbData =myPilImageCopyRGB.tostring()
        myWxImage.SetData( myPilImageRgbData )
        myWxImage.SetAlphaData( myPilImageCopyRGBA.tobytes()[3::4] )  # Create layer and insert alpha values.

    else :    # The resulting image will not have alpha.

        myWxImage = wx.EmptyImage( *myPilImage.size )
        myPilImageCopy = myPilImage.copy()
        myPilImageCopyRGB = myPilImageCopy.convert( 'RGB' )    # Discard any alpha from the PIL image.
        myPilImageRgbData =myPilImageCopyRGB.tobytes()
        myWxImage.SetData( myPilImageRgbData )

    return myWxImage

if __name__ == "__main__":
    class TestFrame(wx.Frame):
        def __init__(self, *args, **kwargs):
            wx.Frame.__init__(self, *args, **kwargs)

            # there needs to be an image here:
            
            # img = img.Rescale(w/2,h/2)
            self.myImage = wx.StaticBitmap(self, -1, pos=(10, 10), size=(240, 400))
            
            # 开始连接
            t = threading.Thread(target=self.onref, args=())
            t.setDaemon(False)
            t.start()
            
        def onref(self):
            while True:
                try:
                    Image = PilImageToWxImageA(messageList.get())
                    # # 添加一张图片显示在x=30，y=50的位置
                    
                    w = Image.GetWidth()
                    h = Image.GetHeight()
                    Image.Rescale(w / 4, h / 4)
                    self.myImage.SetBitmap(Image.ConvertToBitmap())
                except:
                    pass
#             # Using a Sizer to handle the layout: I never like to use absolute postioning
#             box = wx.BoxSizer(wx.VERTICAL)
#             # create the first ImageWindow
#             IW = ImageWindow(Image, self)
#             IW.Proportional = False
#             box.Add(IW, 1, wx.ALL | wx.EXPAND, 10)
#             # create the second ImageWindow
#             IW = ImageWindow(Image, self)
#             IW.Proportional = True
#             IW.BackgroundColor = "Red"
#             box.Add(IW, 1, wx.ALL | wx.EXPAND, 10)

#             self.SetSizer(box)
            
    class App(wx.App):
        def OnInit(self):
            frame = TestFrame(None, title="ImageWindow Test", size=(300, 300))
            self.SetTopWindow(frame)
            frame.Show(True)
            return True

    app = App(False)
    app.MainLoop()