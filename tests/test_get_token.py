# encoding=utf-8
import hashlib
import json
import requests
import time
import pytest
import os


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

    # res = requests.post(url, data=data)
    res = requests.post(url, json=body)
    token = res.json()["result"]["access_token"]
    print(token)
    token_file_base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    token_file_name = "token.txt"
    token_file_path = os.path.join(token_file_base, token_file_name)
    print("token_file_path:", token_file_path)
    file = open(token_file_path, "w")
    file.write(token)
    file.close()
    # print('***---***---***')
    # print(res.content)
    # print('***---***---***')
    # print(json.dumps(res.json(), indent=4))
    # print(res.json()["result"]["access_token"])
    # print(res.json()["result"]["union_id"])

test_get_token()
# 代码合并测试（Mac添加）
# 风帆股份和