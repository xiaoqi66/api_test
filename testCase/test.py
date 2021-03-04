import requests,json,re,time
import jsonpath as js

def upload():
    host = "http://10.10.11.88:9003/handwork/upload.do"
    url = host + ""

    data = {
        "taskCode": "V0201",
        "eventId": "17451"
    }
    files = {"file":open("E:\\lys\\688001_15614.dbf","rb")}
    r = requests.post(url,data=data,files=files)
    # print(r.text)
    return r.json()
aa = upload()
fileName = js.jsonpath(aa,"$..fileName")[0]
remoteFileName = js.jsonpath(aa,"$..remoteFileName")[0]
print(aa)
# print(fileName)
# print(remoteFileName)


def beforeExecuteFtpTask():
    host = "http://sivs.sseinfotest.com:9001"
    url = host+"/handwork/beforeExecuteFtpTask.do"

    data = {"ftpList":[{
        "fileName":fileName,
        "filePath":"/projects/data/sivdc/equity/astock",
        "ftpType":"scheduleFtp",
        "remoteFileName":remoteFileName,
        "remoteFilePath":"./schedule"
    }],
    "method": "post",
    "taskCode": "V0201",
    "voteId": "17451"
    }
    # print(data['ftpList'][0]['fileName'])
    # print(js.jsonpath(data,"$..fileName"))
    # print(data)
    r = requests.post(url,json=data)
    print(r.text)
beforeExecuteFtpTask()


def executeTask():
    url = "http://sivs.sseinfotest.com:9001/egtSchedule/executeTask.do"

    data = {
        "ftpList":[{
        "fileName":fileName,
        "filePath":"/projects/data/sivdc/equity/astock",
        "ftpType":"scheduleFtp",
        "remoteFileName":remoteFileName,
        "remoteFilePath":"./schedule"
    }],
    "method": "post",
    "postTaskReset": True,
    "taskId":100258187
    }
    # print(data['ftpList'][0]['fileName'])
    # print(js.jsonpath(data,"$..fileName"))
    # print(data)
    r = requests.post(url,json=data)
    print(r.text)
executeTask()