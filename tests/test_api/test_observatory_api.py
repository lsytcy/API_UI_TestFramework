import requests
import pytest


class TestMyObsApi:

    def setup(self):
        pass

    def teardown(self):
        pass

    def test_9_day(self):
        url = 'https://pda.weather.gov.hk/locspc/android_data/fnd_e.xml'
        headers = {
            'Host': 'pda.weather.gov.hk',
            'Connection': 'Keep-Alive',
            'Accept-Encoding': 'gzip',
            'User-Agent': 'okhttp/3.12.13 (Android 6.0.1; Netease MuMu) MyObservatory/4.20.1',
            'Cache-Control': 'no-cache'
        }
        response = requests.get(url, headers=headers)
        # 从返回的响应中取出the day after tomorrow相对湿度的值
        max_relative_humidity = response.json()['forecast_detail'][1]["max_rh"]
        min_relative_humidity = response.json()['forecast_detail'][1]["min_rh"]
        print('Relative humidity for the day after tomorrow is ', str(min_relative_humidity) + "-" + str(max_relative_humidity) + "%")
        # 根据forecast_day_of_week的值判断是否是the day after tomorrow的相对湿度
        assert response.json()['forecast_detail'][1]["forecast_day_of_week"] == 2
        assert response.status_code == 200
