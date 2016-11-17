# --*coding:utf-8*--
'''
Created on 2016年11月17日

@author: fanxin, eachen
@note: 
'''
import llxx_app
def getReportListener():
    return llxx_app.llxx_app._llxx_report_listener

def reportError(errorReason):
    getReportListener().onReportError(errorReason)
    
def reportSucess(sucessDes):
    getReportListener().onReportSucess(sucessDes)
