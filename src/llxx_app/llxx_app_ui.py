# --*coding:utf-8*--
'''
Created on 2016年11月27日
@author: fanxin, eachen
@note: 
'''

import wx

class DemoFrame(wx.Frame):
    """ This window displays a button """
    def __init__(self, title=u"llxx自动化测试框架"):
        wx.Frame.__init__(self, None , -1, title)

        self.icon = wx.Icon('res/ic_launcher.ico', wx.BITMAP_TYPE_ICO)
        self.SetIcon(self.icon)  

        MenuBar = wx.MenuBar()

        FileMenu = wx.Menu()
        
        item = FileMenu.Append(wx.ID_EXIT, text=u"&退出")
        self.Bind(wx.EVT_MENU, self.OnQuit, item)

        item = FileMenu.Append(wx.ID_ANY, text=u"&打开")
        self.Bind(wx.EVT_MENU, self.OnOpen, item)

        item = FileMenu.Append(wx.ID_PREFERENCES, text=u"&配置")
        self.Bind(wx.EVT_MENU, self.OnPrefs, item)

        MenuBar.Append(FileMenu, u"&文件")
        
        HelpMenu = wx.Menu()

        item = HelpMenu.Append(wx.ID_HELP, u"帮助",
                                "Help for this simple test")
        self.Bind(wx.EVT_MENU, self.OnHelp, item)

        # # this gets put in the App menu on OS-X
        item = HelpMenu.Append(wx.ID_ABOUT, u"&关于",
                                "More information About this program")
        self.Bind(wx.EVT_MENU, self.OnAbout, item)
        MenuBar.Append(HelpMenu, u"&帮助")

        self.SetMenuBar(MenuBar)

        btn = wx.Button(self, label=u"退出")

        btn.Bind(wx.EVT_BUTTON, self.OnQuit)

        self.Bind(wx.EVT_CLOSE, self.OnQuit)

        s = wx.BoxSizer(wx.VERTICAL)
        s.Add((200, 50))
        s.Add(btn, 0, wx.CENTER, wx.ALL, 20)
        s.Add((200, 50))

        self.SetSizerAndFit(s)
        
    def OnQuit(self, Event):
        self.Destroy()
        
    def OnAbout(self, event):
        dlg = wx.MessageDialog(self, "This is a small program to test\n"
                                     "the use of menus on Mac, etc.\n",
                                "About Me", wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()

    def OnHelp(self, event):
        dlg = wx.MessageDialog(self, "This would be help\n"
                                     "If there was any\n",
                                "Test Help", wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()

    def OnOpen(self, event):
        dlg = wx.MessageDialog(self, "This would be an open Dialog\n"
                                     "If there was anything to open\n",
                                "Open File", wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()

    def OnPrefs(self, event):
        dlg = wx.MessageDialog(self, "This would be an preferences Dialog\n"
                                     "If there were any preferences to set.\n",
                                "Preferences", wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()
        
class MyApp(wx.App):
    def __init__(self, *args, **kwargs):
        wx.App.__init__(self, *args, **kwargs)
        
        # This catches events when the app is asked to activate by some other
        # process
        self.Bind(wx.EVT_ACTIVATE_APP, self.OnActivate)

    def OnInit(self):

        frame = DemoFrame()
        frame.Show()

        import sys
        for f in  sys.argv[1:]:
            self.OpenFileMessage(f)

        return True

    def BringWindowToFront(self):
        try:  # it's possible for this event to come when the frame is closed
            self.GetTopWindow().Raise()
        except:
            pass
        
    def OnActivate(self, event):
        # if this is an activate event, rather than something else, like iconize.
        if event.GetActive():
            self.BringWindowToFront()
        event.Skip()
    
    def OpenFileMessage(self, filename):
        dlg = wx.MessageDialog(None,
                               "This app was just asked to open:\n%s\n" % filename,
                               "File Dropped",
                               wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()

    def MacOpenFile(self, filename):
        """Called for files droped on dock icon, or opened via finders context menu"""
        print filename
        print "%s dropped on app" % (filename)  # code to load filename goes here.
        self.OpenFileMessage(filename)
        
    def MacReopenApp(self):
        """Called when the doc icon is clicked, and ???"""
        self.BringWindowToFront()

    def MacNewFile(self):
        pass
    
    def MacPrintFile(self, file_path):
        pass
 


app = MyApp(False)
app.MainLoop()


