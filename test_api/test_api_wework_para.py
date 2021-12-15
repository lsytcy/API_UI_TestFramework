import requests
import pytest


def test_token():
    corpid = 'wwc0794d551700b367'
    corpsecret = 'ZRqRI3vbH3Le3mOqzxNhb5UejxzV5AFOvgU9yE8Awno'
    # url = f'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}'
    url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=%s&corpsecret=%s' % (corpid, corpsecret)
    r = requests.get(url)
    # print(r.status_code)
    print(r.json())
    # print(r.json()['access_token'])
    # print(r.text)
    return r.json()['access_token']


def test_get(userid):
    # userid = 'YongHuMing2680'
    url = f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={test_token()}&userid={userid}"
    res = requests.get(url)
    print(res.json())
    return res.json()


def test_create(userid, name, mobile):
    data = {
        "userid": userid,
        "name": name,
        "mobile": mobile,
        "department": [1]
    }
    url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={test_token()}"
    res = requests.post(url, json=data)
    print(res.json())
    return res.json()


def test_update():
    data = {
        "userid": "zhangsan",
        "name": "小弟弟",
        "mobile": "+86 13800001234",
        "department": [1]
    }
    url = f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={test_token()}"
    res = requests.post(url, json=data)
    print(res.json())
    return res.json()


def test_delete():
    userid = 'zhangsan'
    url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={test_token()}&userid={userid}"
    res = requests.get(url)
    print(res.json)


@pytest.mark.parametrize("userid, name, mobile",
                         [("zhangsan", "小红", "18912345678")])
def test_all(userid, name, mobile):
    # test_create(userid, name, mobile)
    assert "created" == test_create(userid, name, mobile)['errmsg']
    assert name == test_get(userid)['name']



