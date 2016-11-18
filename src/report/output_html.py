# --*coding:utf-8*--
import codecs
import os
import datetime
import multiprocessing
import collections

import jinja2

if __name__ == '__main__':
    jinja = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname("templates")),
                    trim_blocks=True, lstrip_blocks=True)
    print os.path.dirname(__file__)
    error_report_file_name = os.path.realpath("test.html")
    error_report_file = codecs.open(error_report_file_name, 'w',
                                     "utf-8", 'replace')
    print os.path.basename("templates/report.jinja2")
    
    stats = {}
    
    stats = {   
                'errors': 0,
                'failures': 2,
                'passes': 1,
                'skipped': 0
            }
    stats['encoding'] = "utf-8"
    stats['testsuite_name'] = "测试"
    stats['total'] = (stats['errors'] + stats['failures']
                               + stats['passes'] + stats['skipped'])
    
    manager = multiprocessing.Manager()
    errorlist = manager.list()
    
    errorlist.append({
    'failed': False,
    'class': u"成功测试",
    'name': u"测试1",
    'time': str(datetime.timedelta()),
    'type' : 'passes',
    'exception': '',
    'stdout': "stdout",
    'stderr': "stderr",
    'shortDescription': None,
    'message' : u'pass:[ text:Toast ][ performClick ]\n' + 
        u'pass:[ id:com.llxx.service:id/username ][ inputText:大繁星星 ]\n' + 
        u'pass:[ id:com.llxx.service:id/password ][ inputText:写了个密码 ]\n' + 
        u'pass:[ id:com.llxx.service:id/password ][ requestFocus ]\n' + 
        u'pass:[ id:com.llxx.service:id/password ][ clearFocus ]\n' + 
        u'pass:[ text:Toast ][ performLongClick ]\n'
    })
    
    errorlist.append({
    'failed': True,
    'class': u"失败测试",
    'name': u"测试1",
    'time': str(datetime.timedelta()),
    'type': 'failures',
    'exception': '',
    'message': u"因为失败",
    'stdout': "stdout",
    'stderr': "stderr",
    'shortDescription': None,
    })
    
    errorlist.append({
    'failed': True,
    'class': u"失败测试2",
    'name': u"测试1",
    'time': str(datetime.timedelta()),
    'type': 'failures',
    'exception': '',
    'message': u"因为失败",
    'stdout': "stdout",
    'stderr': "stderr",
    'shortDescription': None,
    })
     
    # sort all class names
    classes = [x['class'] for x in errorlist]
    class_stats = {'failures':0, 'errors':0, 'skipped':0, 'passes':0, 'total':0}
    classes.sort()
    report_jinja = collections.OrderedDict()
    for _class_ in classes:
        report_jinja.setdefault(_class_, {})
        _class_stats_ = class_stats.copy()
        for _error_ in errorlist:
            if _class_ != _error_['class']:
                continue
            report_jinja[_class_].setdefault('tests', [])
            if _error_ not in report_jinja[_class_]['tests']:
                report_jinja[_class_]['tests'].append(_error_)
            _class_stats_[_error_['type']] += 1
        _class_stats_['total'] = sum(_class_stats_.values())
        report_jinja[_class_]['stats'] = _class_stats_
        
    error_report_file.write(jinja.get_template("templates/report.jinja2").render(
                html_title="测试报告",
                stats=stats,
                report=report_jinja,
                start_time=str("11111"),
                duration=str("12"),
                ))
