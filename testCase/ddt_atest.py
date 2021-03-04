# coding=utf-8
import json,jsonpath,time,re
from interface.testfengzhuang import TestApi
from Public.get_excel import makedata
import ddt,unittest
from Public.log import logger,LOG
from Public.MyTest import MyTest


# 加载测试用例文档数据
date_test=makedata('回归_interface_20200927.xls',1)
LOG.info("加载测试用例数据：{}".format(date_test))
# date_test.pop(3)
# date_test.pop(3)
# date_test.pop(3)
# LOG.info("加载测试用例数据：{}".format(date_test))
# lists = []

@ddt.ddt
class Atest(MyTest):
    """项目名称【自动化统计系统】"""

    @ddt.data(*date_test)
    @logger("test_atest_api")
    def test_atest_api(self,date):
        # LOG.info("输入参数：{}".format(date['url']))
        try:
            ASD
        except NameError as msg:
            pass
        # 对excel取到的请求参数进行初步格式判断
        if date['preset'] !="":
            pass
        if date['header'] != "":
            pass
        if date['depend'] != "":
            case_id_list = []
            header_case_id_list = []
            case_id_result_list = []
            header_case_id_result_list = []
            case_id_depent_list = []
            header_case_id_depent_list = []
            # 依赖关系中获取所有jsonpath结果集
            case_id_depent_list_all = []
            header_case_id_depent_list_all = []
            # 依赖关系不为空时，根据依赖关系取相应值并回写到请求参数date['parame']中
            if "%s" in date['parame'] or "%d" in date['parame'] or date['parame'] =="":
                dependdict = date['depend'].split("\n")
                # print("预置条件:", dependdict)
                for dep in range(len(dependdict)):
                    # print("depend参数:",dependdict[dep])
                    # print(type(dependdict[dep]))
                    try:
                        if "header" not in dependdict[dep]:
                            case_id = [ca for ca in json.loads(dependdict[dep].strip("parame:")).keys()][0]
                            case_id_list.append(case_id)
                            case_depend = [ca for ca in json.loads(dependdict[dep].strip("parame:")).values()][0]
                            case_id_depent_list.append(case_depend)
                        else:
                            header_case_id = [ca for ca in json.loads(dependdict[dep].strip("header:")).keys()][0]
                            header_case_depend = [ca for ca in json.loads(dependdict[dep].strip("header:")).values()][0]
                            header_case_id_list.append(header_case_id)
                            header_case_id_depent_list.append(header_case_depend)
                    except Exception as msg:
                        raise NameError("依赖关系写法可能有误 %s" %msg)
                        # print("header_case_id:", header_case_id)
                        # print("header_case_depend:", header_case_depend)
                # print("case_id_list:", case_id_list)
                # print("case_id_depent_list:", case_id_depent_list)
                # print("header_case_id_list:", header_case_id_list)
                # print("header_case_id_depent_list:", header_case_id_depent_list)
                # parame依赖的用例请求结果集
                for caseid in case_id_list:
                    for excel_date in date_test:
                        for k, v in excel_date.items():
                            if v == caseid:
                                # print("excel_date", excel_date)
                                # print("依赖caseid：",caseid)
                                js_result = jsonpath.jsonpath(excel_date, "$..result")
                                # 依赖的用例请求结果
                                # print("依赖的用例请求结果",js_result)
                                case_id_result_list.append(js_result)
                # header依赖的用例请求结果集
                for header_caseid in header_case_id_list:
                    for excel_date in date_test:
                        for k, v in excel_date.items():
                            if v == header_caseid:
                                header_js_result = jsonpath.jsonpath(excel_date, "$..result")
                                # header依赖的用例请求结果
                                # print("header依赖的用例请求结果",header_js_result)
                                header_case_id_result_list.append(header_js_result)
                # parame参数%s对应的参数值
                for cadp in range(len(case_id_depent_list)):
                    if len(case_id_depent_list[cadp]) > 1:
                        for cadp_value in case_id_depent_list[cadp]:
                            jsonpath_result = jsonpath.jsonpath(case_id_result_list[cadp], cadp_value)[0]
                            case_id_depent_list_all.append(jsonpath_result)
                    else:
                        # print(case_id_result_list[cadp])
                        cadp_value = case_id_depent_list[cadp][0]
                        # print(cadp_value)
                        # 从返回值中按照特殊字符@进行切片取需要的值，如短信中包含汉字和数字，取数字作为需要的参数
                        if "@" in cadp_value:
                            jsonpath_result = jsonpath.jsonpath(case_id_result_list[cadp], cadp_value.split("@")[0])[0]
                            cadp_value_txt = cadp_value.split("@")[1].strip("[").strip("]")
                            if cadp_value_txt.split(":")[1] != "":
                                # print(jsonpath_result[int(cadp_value_txt.split(":")[0]):int(cadp_value_txt.split(":")[1])])
                                jsonpath_result = jsonpath_result[int(cadp_value_txt.split(":")[0]):int(cadp_value_txt.split(":")[1])]
                            else:
                                # print(jsonpath_result[int(cadp_value_txt.split(":")[0])::])
                                jsonpath_result = jsonpath_result[int(cadp_value_txt.split(":")[0])::]
                        else:
                            jsonpath_result = jsonpath.jsonpath(case_id_result_list[cadp], cadp_value)[0]

                        if jsonpath_result == False or jsonpath_result == []:
                            raise NameError("依赖关系的jspath语法可能有误，jspath语法为：%s 查询结果为：%s 用例编号：%s" % (
                            cadp_value, jsonpath_result, date['id']))
                        else:
                            case_id_depent_list_all.append(jsonpath_result)

                # header参数%s对应参数值
                for header_cadp in range(len(header_case_id_depent_list)):
                    if len(header_case_id_depent_list[header_cadp]) > 1:
                        for header_cadp_value in header_case_id_depent_list[header_cadp]:
                            header_jsonpath_result = jsonpath.jsonpath(header_case_id_result_list[header_cadp], header_cadp_value)[0]
                            header_case_id_depent_list_all.append(header_jsonpath_result)
                    else:
                        header_cadp_value = header_case_id_depent_list[header_cadp][0]
                        # 从返回值中按照特殊字符@进行切片取需要的值，如短信中包含汉字和数字，取数字作为需要的参数
                        if "@" in header_cadp_value:
                            header_jsonpath_result = jsonpath.jsonpath(header_case_id_result_list[header_cadp], header_cadp_value.split("@")[0])[0]
                            header_cadp_value_txt = header_cadp_value.split("@")[1].strip("[").strip("]")
                            if header_cadp_value_txt.split(":")[1] != "":
                                # print(header_jsonpath_result[int(header_cadp_value_txt.split(":")[0]):int(header_cadp_value_txt.split(":")[1])])
                                header_jsonpath_result = header_jsonpath_result[int(header_cadp_value_txt.split(":")[0]):int(header_cadp_value_txt.split(":")[1])]
                            else:
                                # print(header_jsonpath_result[int(header_cadp_value_txt.split(":")[0])::])
                                header_jsonpath_result = header_jsonpath_result[int(header_cadp_value_txt.split(":")[0])::]
                        else:
                            header_jsonpath_result = jsonpath.jsonpath(header_case_id_result_list[header_cadp], header_cadp_value)[0]
                        # print("jsonpath_result:",jsonpath_result)
                        if header_jsonpath_result == False or header_jsonpath_result == []:
                            raise NameError("依赖关系的jspath语法可能有误，jspath语法为：%s 查询结果为：%s 用例编号：%s" % (
                            header_cadp_value, header_jsonpath_result, date['id']))
                        else:
                            header_case_id_depent_list_all.append(header_jsonpath_result)

                date['header'] = date['header'] % tuple(header_case_id_depent_list_all)
                date['parame'] = date['parame'] % tuple(case_id_depent_list_all)
                # print("date['parame']:",date['parame'])
                # print("date['header']:",date['header'])
        nowtime = time.strftime("%Y-%m-%d")
        api = TestApi(
            ids=date['id'],
            casenames=date['casename'],
            presets=date['preset'],
            headers=date['header'],
            depend=date['depend'],
            url=date['url'],
            parame=date['parame'],
            patype=date['patype'],
            method=date['method'],
            yq=date['yq'],
        )
        result = str(date['yq'])
        if date['parame'] != "":
            # print("api",api.testapi())
            apijson = api.getJson()
        else:apijson = api.getJson()
        # 请求结果回写date_test
        index = date_test.index(date)
        date_test[index]["result"] = apijson
        # date_test[index]["cookie"] = api.getCookie()
        # print(date_test)
        if date['patype'] == "application/json" or date['patype'] == "JSON":
            pass
        elif date['patype'] == "multipart/form-data" or date['patype'] == "DATA":
            apijson = apijson[0]

        if re.search("\n",result):
            for i in result.split("\n"):
                key = i.split("=")[0].strip('"').strip("'")
                val = i.split("=")[1].strip('"').strip("'").strip(",").strip("，").strip(";").strip("；")
                if key.strip("$..").split(".")[-1] not in str(apijson):
                    raise NameError("接口返回结果不存在要验证的KEY值，用例编号：%s" % date['id'])
                else:
                    jsonresult = jsonpath.jsonpath(apijson, key)
                    # print("apijson:", jsonresult)
                    # print("result1:", val, str(jsonresult))
                    if jsonresult == False:
                        raise NameError("jsonpath结果有误，请检查参数及参数类型[%s,%s],[%s,%s]" %(apijson[0:10],type(apijson),key,type(key)))
                    self.assertIn(val, str(jsonresult[0]),"断言失败，用例编号：%s" % date['id'])
            LOG.info("断言成功，用例编号：{}".format(date['id']))
        elif result == "":
            pass
        else:
            key = result.split("=")[0].strip('"').strip("'")
            val = result.split("=")[1].strip('"').strip("'")
            if key.strip("$..").split(".")[-1] not in str(apijson):
                raise NameError("接口返回结果不存在要验证的KEY值，用例编号：%s" % date['id'])
            else:
                jsonresult = jsonpath.jsonpath(apijson, key)
                self.assertIn(val, str(jsonresult[0]),"断言失败，用例编号：%s" % date['id'])
                LOG.info("断言成功，用例编号：{}".format(date['id']))


if __name__ == '__main__':
    unittest.main()