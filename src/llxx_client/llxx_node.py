# --*coding:utf-8*--
'''
Created on 2016年9月12日

@author: fanxin, eachen
'''

# ##
class bounds:
    def __init__(self, boundsStr):
        repStr = boundsStr.replace("][", ",").replace("[", "").replace("]", "");
        result = repStr.split(",")
        self._left = result[0]
        self._top = result[1]
        self._right = result[2]
        self._bottom = result[3]
    
    def left(self):
        return int(self._left)
    
    def top(self):
        return int(self._top)
    
    def right(self):
        return int(self._right)
    
    def bottom(self):
        return int(self._bottom)
    
    def centerTopToBottom(self):
        return " " + str(self.centerX()) + " " + str(self.top() + 10) + " " + str(self.centerX()) + " " + str(self.bottom())
    
    def centerBottomToTop(self):
        return " " + str(self.centerX()) + " " + str(self.bottom() - 10) + " " + str(self.centerX()) + " " + str(self.top())
    
    def centerLeftToRight(self):
        return " " + str(self.left() + 10) + " " + str(self.centerY()) + " " + str(self.right()) + " " + str(self.centerY())
    
    def centerRightToLeft(self):
        return " " + str(self.right() - 10) + " " + str(self.centerY()) + " " + str(self.left()) + " " + str(self.centerY())
    
    def centerX(self):
        return (self.left() + self.right()) / 2
    
    def centerY(self):
        return (self.top() + self.bottom()) / 2
    
    def center(self):
        return " " + str(self.centerX()) + " " + str(self.centerY())