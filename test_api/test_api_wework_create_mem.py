import requests


class TestWeWorkAPI:

    def test_get_token(self):
        corpid = 'wwc0794d551700b367'
        corpsecret = 'ZRqRI3vbH3Le3mOqzxNhb5UejxzV5AFOvgU9yE8Awno'
        """
        两种格式化传参的方式
        1、通过%S传递字符串形式的参数
        2、在字符串前面添加f,通过变量引用传递参数
        """
        url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=%s&corpsecret=%s' % (corpid, corpsecret)
        #url = f'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}'
        r = requests.get(url)
        # print(r.status_code)
        # print(r.json())
        # print(r.json()['access_token'])
        # print(r.text)
        return r.json()['access_token']

    def test_get_mem(self):
        userid = 'YongHuMing2680'
        # 通过调用test_get_token()方法获取token实现参数关联
        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={self.test_get_token()}&userid={userid}'
        r = requests.get(url)
        print(r.json())

# def test_get_token():
#     corpid = 'wwc0794d551700b367'
#     corpsecret = 'ZRqRI3vbH3Le3mOqzxNhb5UejxzV5AFOvgU9yE8Awno'
#     url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=%s&corpsecret=%s' % (corpid, corpsecret)
#     #url = f'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}'
#     r = requests.get(url)
#     # print(r.status_code)
#     # print(r.json())
#     # print(r.json()['access_token'])
#     # print(r.text)
#     return r.json()['access_token']
#
#
# def test_get_mem():
#     userid = 'YongHuMing2680'
#     url = f'https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={test_get_token()}&userid={userid}'
#     r = requests.get(url)
#     print(r.json())