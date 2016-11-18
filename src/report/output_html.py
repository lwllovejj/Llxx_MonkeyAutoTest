# --*coding:utf-8*--
import codecs
import os
import datetime
import multiprocessing
import collections

import jinja2
import sys
import time_utils


if sys.version_info[:2] < (3, 0):
    def force_unicode(s, encoding='UTF-8'):
        try:
            s = unicode(s)
        except UnicodeDecodeError:
            s = str(s).decode(encoding, 'replace')

        return s
else:
    def force_unicode(s, encoding='UTF-8'):
        return str(s)
    
def exc_message(exeinfo):
    return exeinfo.decode("utf-8", 'replace')

class TestReportUnit:
    
    ERROR = 1  # 错误
    PASS = 2  # 通过
    FAIL = 3  # 失败
    SKIP = 4  # 跳过
    
    unit = {'failed': True,
    'class': u"",
    'name': u"",
    'time': str(datetime.timedelta()),
    'type': 'failures',
    'exception': '',
    'message': u"",
    'stdout': "stdout",
    'stderr': "stderr",
    'shortDescription': None
    }
    
    status = PASS
    def __init__(self):
        pass
        
    '''
    @note: 设置是否成功
    '''
    def setStatus(self, status):
        self.status = status
        
        if status == TestReportUnit.PASS:
            self.unit['type'] = 'passes'
            self.unit['failed'] = False
            
        elif status == TestReportUnit.FAIL:
            self.unit['type'] = 'failures'
            self.unit['failed'] = True
            
        elif status == TestReportUnit.ERROR:
            self.unit['type'] = 'failures'
            self.unit['failed'] = True
        
        elif status == TestReportUnit.SKIP:
            self.unit['type'] = 'skip'
            self.unit['failed'] = False
            
        return self
    
    '''
    @note: 设置类别
    '''
    def setClass(self, classname):
        self.unit['class'] = classname
        return self

    '''
    @note: 设置测试的名字
    '''
    def setName(self, testname):
        self.unit['name'] = testname
        return self
    
    '''
    @note: 设置消息
    '''
    def setMessage(self, message):
        self.unit['message'] = message
        return self
    
    '''
    @note: 获取当前单元测试的报告
    '''
    def getReport(self):
        return self.unit
    
    '''
    @note: 设置经过的时长
    '''
    def setTime(self, duratoin):
        self.unit['time'] = duratoin

        
class OutPutReport:
    
    stats = {   
            'errors': 0,
            'failures': 0,
            'passes': 0,
            'skipped': 0
        }
    
    def __init__(self, filename):
        self.html_template = os.path.join(os.path.dirname(__file__), "templates", "report.jinja2")
        self.jinja = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(self.html_template)),
                    trim_blocks=True, lstrip_blocks=True)
        
        self._reportfile = filename
        
        # manager = multiprocessing.Manager()
        # self.reportList = manager.list()
        self.reportList = []
        
        self._starttime = time_utils.getTime()
        self._title = u'测试报告'
        pass
    
    '''
    @note: 
    @param reportUnit: TestReportUnit
    '''
    def addTestReport(self, reportUnit):
        self.reportList.append(reportUnit.getReport())
        if reportUnit.status == TestReportUnit.PASS:
            self.stats['passes'] += 1
            
        elif reportUnit.status == TestReportUnit.FAIL:
            self.stats['failures'] += 1
            
        elif reportUnit.status == TestReportUnit.ERROR:
            self.stats['errors'] += 1
            
        elif reportUnit.status == TestReportUnit.SKIP:
            self.stats['skipped'] += 1
        pass
    
    def setStartTime(self):
        self._starttime = time_utils.getTime()
        print str(self._starttime)
        pass
    
    def printReport(self):
        #
        report_file_name = os.path.realpath(self._reportfile)
        report_file = codecs.open(report_file_name, 'w',
                                 "utf-8", 'replace')
        
        
        self.stats['encoding'] = "utf-8"
        self.stats['testsuite_name'] = "测试"
        self.stats['total'] = (self.stats['errors'] + self.stats['failures']
                                   + self.stats['passes'] + self.stats['skipped'])
        
        # sort all class names
        classes = [x['class'] for x in self.reportList]
        class_stats = {'failures':0, 'errors':0, 'skipped':0, 'passes':0, 'total':0}
        
        
        classes.sort()
        report_jinja = collections.OrderedDict()
        for _class_ in classes:
            report_jinja.setdefault(_class_, {})
            _class_stats_ = class_stats.copy()
            for _error_ in self.reportList:
                if _class_ != _error_['class']:
                    continue
                report_jinja[_class_].setdefault('tests', [])
                if _error_ not in report_jinja[_class_]['tests']:
                    report_jinja[_class_]['tests'].append(_error_)
                _class_stats_[_error_['type']] += 1
            _class_stats_['total'] = sum(_class_stats_.values())
            report_jinja[_class_]['stats'] = _class_stats_
            
        report_file.write(self.jinja.get_template(os.path.basename(self.html_template)).render(
                    html_title=self._title,
                    stats=self.stats,
                    report=report_jinja,
                    start_time=str(self._starttime),
                    duration_time=str(time_utils.getTime() - self._starttime),
                    ))
