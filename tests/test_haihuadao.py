import json
import unittest
import requests
import os


class TestHaiHuaDao(unittest.TestCase):

    def setUp(self):
        self.s = requests.session()
        self.url = 'https://hhd.evergrande.com/zh-cn/'
        file = open(os.path.join((os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "token.txt"), "r")
        token = file.read()
        self.token = token

    def test_visit_haihuadao(self):
        result = self.s.get(self.url)
        assert result.status_code == 200
        print(result.text)
        unittest.TestCase.assertIn(self, '海花岛', result.text)

    def test_get_promote_list(self):
        message_url = 'https://hhd-test-egcapp.evergrande.cn/api/msg/promote/list'
        header = {
            'Host': 'hhd-test-egcapp.evergrande.cn',
            'terminalVersion': '2.6.4',
            'FrontType': 'egc-mobile-ui',
            'Authorization': self.token,
            'Project': 'HHD',
            'Accept': '*/*',
            'appVersion': 'V2.6.4',
            'unionId': 'BDFE6A26F38F394E740D18900627C735',
            'terminalType': 'ios',
            'Accept-Language': 'zh-cn',
            'parkUuid': 'hhd',
            'Accept-Encoding': 'gzip',
            'Content-Type': 'application/json',
            'traceId': '163608116502502001516480BDFE6A26F38F394E740D18900627C735',
            'User-Agent': 'SmartTourism/2.6.4 (iPhone; iOS 14.4; Scale/3.00)',
            'Content-Length': '43',
            'Connection': 'keep-alive',
            'Device': '1',
            'Cookie': ''
        }
        data = json.dumps({"areaCode": "86", "qryTime": 0, "pageSize": 20})
        # 直接带登录态发送请求
        result = self.s.post(message_url, headers=header, data=data)
        print(result.status_code)
        print(json.loads(result.content))
        print(json.loads(result.content)['code'])
        print(self.token)
        assert result.status_code == 200

    def test_api_cms_news_list(self):
        cms_news_list_url = "https://hhd-test-egcapp.evergrande.cn/api/cms/news/list"
        headers = {
            'Host': 'hhd-test-egcapp.evergrande.cn',
            'terminalVersion': '2.6.4',
            'FrontType': 'egc-mobile-ui',
            'Authorization': self.token,
            'Project': 'HHD',
            'Accept': '*/*',
            'appVersion': 'V2.6.4',
            'unionId': '9D6B655E8D1A2A0843C40153DB8BD1F7',
            'terminalType': 'ios',
            'Accept-Language': 'zh-cn',
            'parkUuid': 'hhd',
            'Accept-Encoding': 'gzip',
            'Content-Type': 'application/json',
            'traceId': '1635921795303020044162829D6B655E8D1A2A0843C40153DB8BD1F7',
            'Content-Length': '49',
            'User-Agent': 'SmartTourism/2.6.4 (iPhone; iOS 14.4; Scale/3.00)',
            'Connection': 'keep-alive',
            'Device': '1'
        }
        data = json.dumps({"module": "app_001", "pageSize": 3, "areaCode": "86"})
        result = self.s.post(cms_news_list_url, headers=headers, data=data)
        print(result.status_code)
        print(result.json)
        print(result.text)
        print(json.loads(result.content)['code'])
        print((json.loads(result.content)['data'][1]['summary']))
        assert result.status_code == 200
        #assert json.loads(result.code) == 00000

    def tearDown(self):
        self.s.close()


if __name__ == "__main__":
    unittest.main(verbosity=2)