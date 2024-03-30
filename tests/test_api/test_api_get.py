from pip._vendor import requests


#
class TestDemo:
    def test_json_demo(self):
        url = 'https://ceshiren.com/categories.json'
        r = requests.get(url)
        assert r.json()['category_list']['categories'][0]['topic_count']== 1568

    def test_json_post(self):
        payload = {
            'level': 1,
            'name': 'lsytcy'
        }
        url = 'https://httpbin.testing-studio.com/post'
        # verify=False防止因为证书问题导致报错
        r = requests.post(url, json=payload, verify=False)
        print(r.status_code)
        assert r.status_code == 200

