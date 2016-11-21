# --*coding:utf-8*--
'''
Created on 2016年11月21日

@author: fanxin, eachen
描述Usb设备
# 参考AutomatorX https://github.com/xiaoyaojjian/AutomatorX.git
'''
import re

class Device:

    def __init__(self, client, serial):
        ''' TODO: client change to host, port '''
        self._client = client
        self._serial = serial

    @property
    def serial(self):
        return self._serial
    
    def raw_cmd(self, *args, **kwargs):
        args = ['-s', self._serial] + list(args)
        return self._client.raw_cmd(*args, **kwargs)

    def run_cmd(self, *args, **kwargs):
        """
        Unix style output, already replace \r\n to \n

        Args:
            - timeout (float): timeout for a command exec
        """
        timeout = kwargs.pop('timeout', None)
        p = self.raw_cmd(*args, **kwargs)
        return p.communicate(timeout=timeout)[0].replace('\r\n', '\n')

    def shell(self, *args, **kwargs):
        """
        Run command `adb shell`
        """
        args = ['shell'] + list(args)
        return self.run_cmd(*args, **kwargs)
    
    def current_app(self):
        """
        Return: dict(package, activity, pid?)
        Raises:
            RuntimeError
        """
        # try: adb shell dumpsys activity top
        _activityRE = re.compile(r'ACTIVITY (?P<package>[^/]+)/(?P<activity>[^/\s]+) \w+ pid=(?P<pid>\d+)')
        m = _activityRE.search(self.shell('dumpsys', 'activity', 'top'))
        if m:
            return dict(package=m.group('package'), activity=m.group('activity'), pid=int(m.group('pid')))

        # try: adb shell dumpsys window windows
        _focusedRE = re.compile('mFocusedApp=.*ActivityRecord{\w+ \w+ (?P<package>.*)/(?P<activity>.*) .*')
        m = _focusedRE.search(self.shell('dumpsys', 'window', 'windows'))
        if m:
            return dict(package=m.group('package'), activity=m.group('activity'))
        raise RuntimeError("Couldn't get focused app")
    
