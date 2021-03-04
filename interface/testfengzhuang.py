# coding=utf-8
from interface.test_requests import requ
import json,xmltodict,time
from Public.log import *


reques=requ()


class TestApi(object):
    def __init__(self,ids,casenames,presets,headers,depend,url,parame,patype,method,yq):
        self.ids=ids
        self.casenames=casenames
        self.presets=presets
        self.headers=headers
        self.depend=depend
        self.url=url
        self.parame=parame
        self.patype=patype
        self.method=method
        self.yq=yq
        # self.voteid=voteid

    def testapi(self):
        # print(self.method)
        LOG.info("用例编号：{}".format(self.ids))
        LOG.info("用例名称：{}".format(self.casenames))
        LOG.info("请求url：{}".format(self.url))
        LOG.info("预置条件：{}".format(self.presets.replace("\n","||")))
        LOG.info("预置header：{}".format(self.headers))
        LOG.info("依赖关系：{}".format(self.depend.replace("\n","||")))
        LOG.info("请求参数：{}".format(self.parame))
        LOG.info("参数类型：{}".format(self.patype))
        # 对excel请求参数进行初步格式判断
        if self.parame != "":
            # print("self.headers:", self.headers)
            # print("self.parame:", self.parame)
            if "&" in self.parame:
                try:
                    json.loads(self.parame.split("&")[0])
                    json.loads(self.parame.split("&")[1])
                except json.JSONDecodeError as msg:
                    LOG.info("Excel请求参数格式有误，请检查", msg)
            else:
                try:
                    json.loads(self.parame)
                except json.JSONDecodeError as msg:
                    LOG.info("Excel请求参数格式有误，请检查", msg)
        if self.headers != "":
            # print("aaaaaaa")
            try:
                self.headers = json.loads(self.headers)
            except json.JSONDecodeError as msg:
                LOG.info("Excel请求header格式有误，请检查", msg)
        #
        if self.method=='POST':
            LOG.info("请求方式：POST")
            # print(self.parame)
            if self.patype == "application/json" or self.patype == "JSON":
                # print("self.parame:",self.parame)
                if self.parame != "" and self.parame != "{}":
                    parame = json.loads(self.parame)
                else:
                    parame = self.parame
                response=reques.post(self.url,parame,self.headers)
                response_text=response.text
                # response_cookie=response.headers["Set-Cookie"].split(";")[0]
                LOG.info("请求结果：{}".format(response_text.replace("\n","").replace(" ","")))
                LOG.info("预期结果：{}".format(self.yq.replace("\n","||")))
                return response
            elif self.patype == "multipart/form-data" or self.patype == "DATA":
                if "&" in self.parame:
                    # print("aaa",parames)
                    if self.parame != "" and self.parame != "{}":
                        parame = json.loads(self.parame.split("&")[0])
                    else:
                        parame = self.parame
                    files = json.loads(self.parame.split("&")[1])
                    files["file"] = open(files["file"], "rb")
                    response = reques.post(url=self.url, parames=parame,files=files, header=self.headers)
                    response_text = response.text
                    LOG.info("请求结果：{}".format(response_text.replace("\n","").replace(" ","")))
                    LOG.info("预期结果：{}".format(self.yq.replace("\n","||")))
                else:
                    if self.parame != "" and self.parame != "{}":
                        parame = json.loads(self.parame)
                    else:
                        parame = self.parame
                    response = reques.post(self.url, parame, self.headers)
                    response_text = response.text
                    LOG.info("请求结果：{}".format(response_text.replace("\n","").replace(" ","")))
                    LOG.info("预期结果：{}".format(self.yq.replace("\n","||")))
                return response
            elif self.patype == "x-www-form-urlencoded":
                # print(self.patype)
                if self.parame != "" and self.parame != "{}":
                    parame = json.loads(self.parame)
                else:
                    parame = self.parame
                # print("self.parame1111", self.parame)
                # print("self.parame1111", type(self.parame))
                response = reques.post(self.url, parame,header=self.headers,patype=self.patype)
                response_text = response.text
                LOG.info("请求结果：{}".format(response_text.replace("\n", "").replace(" ", "")))
                LOG.info("预期结果：{}".format(self.yq.replace("\n", "||")))
                return response
            else:
                raise NameError("Excel参数类型有误")
        elif self.method=='GET':
            LOG.info("请求方式：GET")
            if self.patype == "application/json" or self.patype == "JSON" or self.patype == "":
                if self.parame != "" and self.parame != "{}":
                    parame = json.loads(self.parame)
                else:
                    parame = self.parame
                response=reques.get(self.url,parame)
                response_text = response.text
                LOG.info("请求结果：{}".format(response_text))
                LOG.info("预期结果：{}".format(self.yq.replace("\n", "||")))
                return response
            else:
                raise NameError("Excel参数类型有误")
        elif self.method=='PUT':
            LOG.info("请求方式：PUT")
            if self.parame != "" and self.parame != "{}":
                parame = json.loads(self.parame)
            else:
                parame = self.parame
            response=reques.put(self.url,parame)
            response_text = response.text
            LOG.info("请求结果：{}".format(response_text))
            LOG.info("预期结果：{}".format(self.yq.replace("\n", "||")))
            return response


    def getCode(self):
        code = self.testapi()["code"]
        return code


    def getCookie(self):
        print("cookie:",self.testapi())
        cookie = self.testapi().headers["Set-Cookie"]
        return cookie


    def getJson(self):

        # print("self.testapi():", self.testapi())
        json_data = self.testapi().text
        # print("json_data",json_data)
        # jsonloads = json.loads(json_data)
        try:
            jsonloads = json.loads(json_data)
            return jsonloads
        except json.JSONDecodeError:
            return json_data
        except Exception as msg:
            raise NameError("接口请求结果无法转换,%s" %msg)
        # return eval(json_data)

    def getXml(self):
        json_data1 = xmltodict.parse(self.testapi())
        return json.loads(json.dumps(json_data1))