# --*coding:utf-8*--
'''
Created on 2016年9月12日

@author: fanxin, eachen
'''

def safeGet(json, keyword):
    if keyword in json.keys():
        return json[keyword];
    return None

class node:
    def __init__(self, nodeJson):
        #{'node': {'index': -1, 'long_clickable': False, 'checked': False, 'clickable': True, 
        #'package': 'com.cloudd.user', 'text': u'\u767b\u5f55', 'selected': False, 'enabled': False, 
        #'bounds': '[108,1468][972,1612]', 'focusable': True, 'windowId': 983, 'focused': False, 
        #'checkable': False, 'resource-id': 'com.cloudd.user:id/tv_login', 'password': False, 
        #'class': 'android.widget.Button', 'scrollable': False}, 'isfind': True}
        self.long_clickable = safeGet(nodeJson, "long_clickable")
        self.checked = safeGet(nodeJson, "checked")
        self.clickable = safeGet(nodeJson, "clickable")
        self.package = safeGet(nodeJson, "package")
        self.text = safeGet(nodeJson, "text")
        self.selected = safeGet(nodeJson, "selected")
        self.enabled = safeGet(nodeJson, "enabled")
        self.checkable = safeGet(nodeJson, "checkable")
        self.resource_id = safeGet(nodeJson, "resource-id")
        self.password = safeGet(nodeJson, "password")
        self.classname = safeGet(nodeJson, "class")
        self.scrollable = safeGet(nodeJson, "scrollable")
        self.isfind = safeGet(nodeJson, "isfind")

    def get_long_clickable(self):
        return self.__long_clickable


    def get_checked(self):
        return self.__checked


    def get_clickable(self):
        return self.__clickable


    def get_package(self):
        return self.__package


    def get_text(self):
        return self.__text


    def get_selected(self):
        return self.__selected


    def get_enabled(self):
        return self.__enabled


    def get_checkable(self):
        return self.__checkable


    def get_resource_id(self):
        return self.__resource_id


    def get_password(self):
        return self.__password


    def get_classname(self):
        return self.__classname


    def get_scrollable(self):
        return self.__scrollable


    def get_isfind(self):
        return self.__isfind


    def set_long_clickable(self, value):
        self.__long_clickable = value


    def set_checked(self, value):
        self.__checked = value


    def set_clickable(self, value):
        self.__clickable = value


    def set_package(self, value):
        self.__package = value


    def set_text(self, value):
        self.__text = value


    def set_selected(self, value):
        self.__selected = value


    def set_enabled(self, value):
        self.__enabled = value


    def set_checkable(self, value):
        self.__checkable = value


    def set_resource_id(self, value):
        self.__resource_id = value


    def set_password(self, value):
        self.__password = value


    def set_classname(self, value):
        self.__classname = value


    def set_scrollable(self, value):
        self.__scrollable = value


    def set_isfind(self, value):
        self.__isfind = value

    long_clickable = property(get_long_clickable, set_long_clickable, None, None)
    checked = property(get_checked, set_checked, None, None)
    clickable = property(get_clickable, set_clickable, None, None)
    package = property(get_package, set_package, None, None)
    text = property(get_text, set_text, None, None)
    selected = property(get_selected, set_selected, None, None)
    enabled = property(get_enabled, set_enabled, None, None)
    checkable = property(get_checkable, set_checkable, None, None)
    resource_id = property(get_resource_id, set_resource_id, None, None)
    password = property(get_password, set_password, None, None)
    classname = property(get_classname, set_classname, None, None)
    scrollable = property(get_scrollable, set_scrollable, None, None)
    isfind = property(get_isfind, set_isfind, None, None)
        
    
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