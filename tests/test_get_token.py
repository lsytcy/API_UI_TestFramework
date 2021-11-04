# encoding=utf-8
import hashlib
import json
import requests
import time
import pytest

def test_get_token():
    # UAT-环境的登录接口url
    domain = " https://uic-uat.evergrande.cn/v1/user/login_pwd?"
    body = {"phone": "17888888801", "pwd": "ef73781effc5774100f87fe2f437a435", "os_type": "Android",
            "app_uuid": "7BE8C23E-9974-4747-B734-8F67029D4C4B"}
    data = json.dumps(body)
    appidtmp = "100007"
    appkeytmp = "@hhd123appkey#"
    timestamp = str(int(time.time()))
    #print(data)
    query_str = "appid=" + appidtmp + "&body=" + data + "&timestamp=" + timestamp
    tmp_sig = query_str + "&appkey=" + appkeytmp
    #print(tmp_sig)
    # md5 调用库函数
    sig = hashlib.md5(tmp_sig.encode(encoding='UTF-8')).hexdigest().upper()
    #print(sig)
    para = "appid=" + appidtmp + "&sig=" + sig + "&timestamp=" + timestamp
    url = domain + para
    #print(url)

    res = requests.post(url, data=data)
    token = res.json()["result"]["access_token"]
    file = open("D:\\python-project\\API_UI_TestFramework\\token.txt", "w")
    file.write(token)
    file.close()
    # print('***---***---***')
    # print(res.content)
    # print('***---***---***')
    # print(json.dumps(res.json(), indent=4))
    # print(res.json()["result"]["access_token"])
    # print(res.json()["result"]["union_id"])
