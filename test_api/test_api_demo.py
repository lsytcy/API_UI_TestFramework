import requests
import pytest
from jsonpath import jsonpath
from hamcrest import *


class TestDemo:

    def test_json_demo(self):
        url = 'https://ceshiren.com/categories.json'
        r = requests.get(url)
        assert r.json()['category_list']['categories'][0]['topic_count']== 535

    def test_json_post(self):
        payload = {
            'level': 1,
            'name': 'lsytcy'
        }
        url = 'https://httpbin.testing-studio.com/post'
        r = requests.post(url, json=payload)
        assert r.status_code == 200

    def test_json_post(self):
        payload = {
            'level': 1,
            'name': 'lsytcy'
        }
        url = 'https://httpbin.testing-studio.com/post'
        r = requests.post(url, json=payload)
        assert r.status_code == 200

    def test_hamcrest(self):
        payload = {
            'level': 1,
            'name': 'lsytcy'
        }
        url = 'https://httpbin.testing-studio.com/post'
        r = requests.post(url, json=payload)
