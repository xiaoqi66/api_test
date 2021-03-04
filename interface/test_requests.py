# coding=utf-8
import requests,json,time


class requ():
    def __init__(self):
        # print("abc")
        pass

    def get(self,url,parames):
        # print("url",url)
        # print("parames",parames)
        # print("parames",type(parames))
        try:
            if parames == "":
                r = requests.get(url)
            else:
                r = requests.get(url,parames)
                # print(r.url)
            return r
        except Exception as e:
            print("get请求出错，出错原因：%s" %e)
            return {}

    def post(self,url,parames,header,files=0,patype=""):
        # print("url", url)
        # print("parames", parames)
        # print("parames", type(parames))
        try:
            if files != 0:
                # print("files:",files)
                r = requests.post(url,data=parames,files=files,headers=header)
                time.sleep(2)
                # return r.text
            elif patype == "x-www-form-urlencoded":
                r = requests.post(url,data=parames,headers=header)
                # print(r.text)
                # return r.text
            elif parames == "" and files==0:
                r = requests.post(url,headers=header)
                # return r.text
            else:
                # print("url:",url)
                # print("parames:",parames)
                # print("parames:",type(parames))
                # print("headers:",header)
                r = requests.post(url,json=parames,headers=header)
                # print("r.text:",r.text)
                # return r.text
            if r.text == "":
                raise NameError("接口请求结果为空，请检查接口")
            return r

        except Exception as e:
            print("post请求出错，出错原因：%s" %e)
            return {}


    def put(self,url,parames):
        try:
            r = requests.put(url,json=parames)
            return r.text
        except Exception as e:
            print("put请求出错，出错原因：%s" %e)
            return {}