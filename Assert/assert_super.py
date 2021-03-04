# coding=utf-8
from Public.log import LOG,logger
from Public.get_dataBase import *

# qiwang = "a=1&b=2&c=sql&s=1"
# fanhui = {'a':1,'b':2,'c':'sql','d':4,'e':5}
# qiwang1 = "name=google&url=www.google.com"
fanhui1 = {"data":{
    "sites": [
    {"name":[1,2,3,4],"url":"www.test.com" },
    {"name":"google","url":"www.google.com"},
    {"name":"weibo","url":"www.weibo.com" },
    {"name":"369","url":"www.weibo.com" }
]}}
# fanhui2 = {"url":"www.test.com", "sites": [{"name":"test","url":"www.test1.com" },{"name":"weibo","url":"www.weibo.com" }]}
#
#
# listfanhui = []
#
# # @logger("make_fanhuidata断言测试结果")
# def make_fanhuidata(dict, objkey):
#     tmp = dict
#     for k,v in tmp.items():
#         if k == objkey:
#             # print v
#             listfanhui.append({k:v})
#             # listfanhui.append(v)
#         else:
#             if type(v) is types.DictType:
#                 make_fanhuidata(v, objkey)
#             elif type(v) is types.ListType:
#                 listfanhui.append(v)
#                 for i in v:
#                     if type(i) is not types.DictType:
#                         listfanhui.append(i)
#                     elif type(i) is types.DictType:
#                         make_fanhuidata(i,objkey)
#     # return listfanhui
# # make_fanhuidata(fanhui1,"name")
# # print listfanhui
#
#
# @logger("assert_in断言测试结果")
# def assert_in(assertqiwang,fanhuijson):
#     if len(assertqiwang.split('='))>1:
#         data = assertqiwang.strip().split('&')
#         # print data
#         itlist = []
#         for item in data:
#             # LOG.info(item)
#             itlist.append(dict([item.split('=')]))
        # print "JSON数据:",fanhui
        # print "期望:",itlist
        # for k,v in fanhuijson.items():
        #     try:
        #         json.loads(v)
        #     except:
        #         pass
        #     for i in itlist:
        #         if k == i.keys()[0]:
        #             if str(v) == str(i.values()[0]):
        #                 # print "pass:",v,i.values()[0]
        #                 return True
        #             else:
        #                 raise NameError("断言失败，期望值:",i.values()[0],"实际值返回值:",v)
                # else:
                #     print None
# assert_in(qiwang,fanhui)

# make_fanhuidata(fanhui2,"url")
# print(listfanhui)


class superAssert(object):

    # def assertEQ(self,left,right):
    #     """
    #     验证left == right
    #     """
    #     le = left[1]
    #     try:
    #         ri = right["{}".format(left[0])]
    #     except KeyError:
    #         LOG.info("断言失败，结果中未找到预期的key值：%s" %left[0])
    #         raise NameError("断言失败，结果中找不到预期的key值：%s" %left[0])
    #     try:
    #         self.assertEqual(le,ri,msg="返回url错误")
    #         LOG.info('断言通过，断言结果：{0} == {1}'.format(le,ri))
    #     except AssertionError as msg:
    #         LOG.info('断言失败，断言结果：{0} != {1}'.format(le,ri))
    #         raise NameError('期望失败：%s' %msg)

    def assertIN(self,left,right,conf=None,sql=None):
        """
        验证right包含left
        """
        # print "'{0}': u'{1}'".format(left[0],left[1])
        # print str(right).strip("u")
        lef = "'{0}': u'{1}'".format(left[0],left[1])
        if lef in str(right):
            LOG.info('断言通过,验证：{}'.format(lef))
        elif left[1] == "{sql}":
                conf = "newtrainmgr/newtrainmgr@10.10.11.40:1521/SITDB"
                sql = "select n.account_id from new_train_apply n where n.train_id='16135' and n.trainee_id='785'"
                # print "'{0}': '{1}'".format(left[0],getOracleBizdevData(conf,sql)[0][0])
                # print str(right)
                sqldata = getOracleBizdevData(conf,sql)[0][0]
                lef = "'{0}': u'{1}'".format(left[0],sqldata)
                if lef in str(right):
                    LOG.info('断言通过,验证：{}'.format(lef))
                else:
                    LOG.info('断言失败，接口返回不符合预期{0}'.format(lef))
                    raise NameError("断言失败")
        else:
            LOG.info('断言失败')
            raise NameError("断言失败")

