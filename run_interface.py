# coding=utf-8

from testCase import ddt_atest
from Public import HTMLTestReportCN
import unittest,time,os


if __name__ == '__main__':

    testsuite = unittest.TestSuite()
    test_dir = os.path.dirname(__file__)+"/testCase/"
    print(test_dir)
    # discover = unittest.defaultTestLoader.discover(test_dir.replace("/","\\"),pattern='*test.py')
    testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(ddt_atest.Atest))
    # testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(sseInternetVote_test.sseInterTest))
    now = time.strftime('%Y-%m-%d %H%M',time.localtime(time.time()))
    basedir = os.path.dirname(__file__)
    file_dir = os.path.join(basedir,'test_Report').replace("\\","/")
    print(file_dir)
    file = os.path.join(file_dir,("每日回归测试报告 "+now+'.html')).replace("\\","/")
    fl_open = open(file,'wb')
    runner = HTMLTestReportCN.HTMLTestRunner(
        stream=fl_open,
        title=u'接口测试报告',
        description=u'测试结果',
        tester = u"yoyo"
    )
    runner.run(testsuite)