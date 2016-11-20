# --*coding:utf-8*--
'''
Created on 2016年11月20日

@author: fanxin, eachen
'''

import cv2
from PIL import Image

DEBUG = False

'''
显示图片
'''
def show(img):
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def imread(filename):
    im = cv2.imread(filename)
    if im is None:
        raise RuntimeError("file: '%s' not exists" % filename)
    return im

if __name__ == '__main__':
     
    #读取底片
    imp = Image.open('data/ic_launcher.png')
    #读取要粘贴的图片 RGBA模式
    imq = Image.open('data/baselib_title_left.png').convert('RGBA')
    #分离通道
    rgba = imq.split()
    #粘贴
    imp.paste(imq, (0,0),mask=rgba[3])
    imp.save('foo_2.jpg', 'JPEG', quality=80)
    
    ## 图片旋转
    #rgbimg = Image.open("data/baselib_title_left.png")
    #rgbimg.rotate(45).show()
    #rgbimg = cv2.imread("data/baselib_title_left.png",0) #直接读为灰度图像
    
    #show(rgbimg)
    
png = Image.open('data/baselib_title_left.png').convert('RGBA')
png.load() # required for png.split()

background = Image.new("RGB", png.size, (0, 0, 0))
background.paste(png, mask=png.split()[3]) # 3 is the alpha channel

background.save('foo.jpg', 'JPEG', quality=80)
# png = Image.open(object.logo.path)
# png.load() # required for png.split()
# 
# background = Image.new("RGB", png.size, (255, 255, 255))
# background.paste(png, mask=png.split()[3]) # 3 is the alpha channel
# 
# background.save('foo.jpg', 'JPEG', quality=80)
