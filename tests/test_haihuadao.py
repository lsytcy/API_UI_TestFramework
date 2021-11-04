import json
import unittest
import requests


class TestHaiHuaDao(unittest.TestCase):

    def setUp(self):
        self.s = requests.session()
        self.url = 'https://hhd.evergrande.com/zh-cn/'

    def test_visit_haihuadao(self):
        result = self.s.get(self.url)
        assert result.status_code == 200
        print(result.text)
        unittest.TestCase.assertIn(self, '海花岛', result.text)

    def test_get_promote_list(self):
        message_url = 'https://hhd-test-egcapp.evergrande.cn/api/msg/promote/list'
        header ={}
        # 直接带登录态发送请求
        result = self.s.get(message_url, cookies=cookie, headers=header)
        assert result.status_code == 200
        assert json.loads(result.content)['message'] == '成功'

    def test_api_cms_news_list(self):
        cms_news_list_url = "https://hhd-test-egcapp.evergrande.cn/api/cms/news/list"
        headers = {
            'Host': 'hhd-test-egcapp.evergrande.cn',
            'terminalVersion': '2.6.4',
            'FrontType': 'egc-mobile-ui',
            'Authorization': '6MOhKH20XWuoShCs4oIQfdWf9iF9pU-WjEv3oQjhKaeQSDAmFbaHbn-pxM3mcANFtHSXABZlWuwt3ebON_4f6X001mowBm0n_AUj-3AydvzuhNSwqa2RYU62bwxHn8h0_sWBogUCFTt6ZVf8MeBg87EQDQOxXIDb9khnRNnd_3nTx9MJBNdWIlXY89vbbKz-TSCkb_5MvkrGh-7aMym70q-36IQtz3-pgFLnXZ9U2HcleQ55xcUPbli-Fdg1sWr_SvUokY4CbTXerTTkXI87m6yY84X8h5exmy9bgY95wr8',
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
        result = self.s.post(cms_news_list_url, headers=headers,data=data)
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