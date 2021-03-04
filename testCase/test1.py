import requests,json,jsonpath

def beforeExecuteFtpTask():
    host = "http://sivs.sseinfotest.com:9001"
    url = host+"/monitor/eventDetail.do"
    print(url)
    data = {
    "eventId":17485,
    "method":"post",
    "taskDate":"2020-07-09"
}

    r = requests.post(url,json=data)
    print(r.text)
    return r.text
aa = beforeExecuteFtpTask()
bb = json.loads(aa)
print(jsonpath.jsonpath(bb,"$..groupList[8].taskList[0].taskId"))
