# coding=utf-8
import unittest,warnings
from log import *
from Public.log import *


class MyTest(unittest.TestCase):
    def setUp(self):
        # 去除ResourceWarning信息
        warnings.simplefilter('ignore', ResourceWarning)
        # LOG.info(u"=" * 75)
        LOG.info(u"测试用例开始执行")

    def tearDown(self):
        LOG.info(u"测试用例执行完毕")
        LOG.info(u"="*75)



