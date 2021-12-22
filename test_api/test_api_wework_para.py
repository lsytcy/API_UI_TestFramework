import os
import random
import re
import requests
import pytest


@pytest.fixture(scope='session')
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


def test_get(userid, test_token):
    # userid = 'YongHuMing2680'
    url = f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={test_token}&userid={userid}"
    res = requests.get(url)
    print(res.json())
    return res.json()


def test_create(userid, name, mobile, test_token):
    data = {
        "userid": userid,
        "name": name,
        "mobile": mobile,
        "department": [1]
    }
    url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={test_token}"
    res = requests.post(url, json=data)
    print(res.json())
    return res.json()

def test_create_data():
    userid = str(random.randint(0,99999999))
    data = [(userid, 'username' + userid, str(random.randint(13800000000, 13899999999))) for x in range(10)]
    print(data)


def test_update(userid, name, mobile, test_token):
    data = {
        "userid": userid,
        "name": name,
        "mobile": mobile,
        "department": [1]
    }
    url = f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={test_token}"
    res = requests.post(url, json=data)
    print(res.json())
    return res.json()


def test_delete(userid, test_token):
    # userid = 'zhangsan'
    url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={test_token}&userid={userid}"
    res = requests.get(url)
    print(res.json)
    return res.json()


@pytest.mark.parametrize("userid, name, mobile",
                         [("wangwu", "小黄", "18911122233")])
def test_all(userid, name, mobile, test_token):
    # test_create(userid, name, mobile)
    try:
        assert "created" == test_create(userid, name, mobile, test_token)['errmsg']
    except AssertionError as e:
        if "existed" in e.__str__():
            re_userid = re.findall(":(.*?)'", e.__str__())[0]
            print(re.findall(":(.*)'", e.__str__()))
            assert "deleted" == test_delete(re_userid, test_token)['errmsg']
            assert 60111 == test_get(userid, test_token)['errcode']
    # assert "created" == test_create(userid, name, mobile)['errmsg']
    assert name == test_get(userid, test_token)['name']
    assert "updated" == test_update(userid, 'GGG', mobile, test_token)['errmsg']
    assert "deleted" == test_delete(userid, test_token)['errmsg']
    assert 60111 == test_get(userid, test_token)['errcode']



