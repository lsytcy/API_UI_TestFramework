import requests
import pytest


class TestDemo:
    @pytest.mark.skip
    def test_get(self):
        r = requests.get('https://api.github.com/events')
        print(r.text)
        print(r.status_code)
        print(r.json())
        assert r.status_code == 200

    @pytest.mark.skip
    def test_get_1(self):
        r = requests.get('https://httpbin.testing-studio.com/get')
        print(r.text)
        print(r.status_code)
        print(r.json())
        assert r.status_code == 200

    def test_post_form(self):
        payload = {
            "level": 1,
            "name": "lsytcy"
        }
        r = requests.post('https://httpbin.testing-studio.com/post', data=payload)
        print(r.text)
        assert r.status_code == 200

    def test_post_json(self):
        payload = {
            "level": 1,
            "name": "lsytcy"
        }
        r = requests.post('https://httpbin.testing-studio.com/post', json=payload)
        print(r.text)
        assert r.status_code == 200
        assert r.json()['json']['level'] == 1

    def test_hgwz_json(self):
        r = requests.post('https://home.testing-studio.com/categories.json')
        print(r.text)
        assert r.status_code == 200

