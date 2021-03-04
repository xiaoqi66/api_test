import requests,json,jsonpath

def beforeExecuteFtpTask():
    url = "http://sivs.sseinfotest.com:9001/egtSchedule/executeTask.do"
    print(url)
    data = {
    "taskId":100267748,
    "method":"post",
    "postTaskReset":True
}

    r = requests.post(url,json=data)
    print(r.text)
    return r.text
# aa = beforeExecuteFtpTask()
# bb = json.loads(aa)
# print(type(bb))
# print("status" in bb)
# print(jsonpath.jsonpath(bb,"$..groupList[2].taskList[2].taskId"))

aa = [1,2,3,4,5]
print([1 or 2] in aa)