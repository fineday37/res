import os
import sys
import json
from lib.readexcle import Readexcel
import requests

sys.path.append(os.path.dirname(os.path.dirname(__file__)))


def sendrequests(apiData):
    try:
        method = apiData["method"]
        url = apiData["url"]
        if apiData["params"] == "":
            par = None
        else:
            par = eval(apiData["params"])
        if apiData["headers"] == "":
            h = None
        else:
            h = eval(apiData["headers"])
        if apiData["body"] == "":
            body_data = None
        else:
            body_data = eval(apiData["body"])
        type = apiData["type"]
        if type == "data":
            body = body_data
        elif type == "json":
            body = json.dump(body_data)
        else:
            body = body_data
        re = requests.request(method=method, url=url, headers=h, params=par, data=body)
        return re
    except Exception as e:
        print(e)


class SendRequests:
    pass


if __name__ == '__main__':
    apiData = Readexcel(r"E:\requests\DemoAPITestCase.xlsx").read_data()
    print(len(apiData))
    for i in range(len(apiData)):
        sendrequests(apiData[i])
