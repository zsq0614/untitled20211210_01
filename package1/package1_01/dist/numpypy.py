#coding=utf-8
import seleniumbase
import requests
from threading import Thread
import json
import pytest

data = [({"city": '上海', "key": "331eab8f3481f37868378fcdc76cb7cd", 'result':"查询成功!"}),
        ({"city": "上海", "key": "331eab8f3481f37868378fcdc76cb7c", 'result':"错误的请求KEY"}),
        ({"city": "上", "key": "331eab8f3481f37868378fcdc76cb7cd", 'result':"暂不支持该城市"})]
class TestCase():
    def weather(self,city,key):
        url = "http://apis.juhe.cn/simpleWeather/query'"
        data = {'city':city, 'key':key}
        print data
        r = requests.post(url,data=data)
        return r.json()
    def shenfenzheng(self,cardno,key):
        data = {"cardno":cardno,"key":key}
        r = requests.post('http://apis.juhe.cn/idcard/index',data=data)
        return r.json()
    @pytest.mark.parametrize('data',data)
    def test_01(self,data):
        r = TestCase().weather(city=data['city'],key=data['key'])
        assert r['reason'] ==data['result']
    def test_02(self):
        cardno = '130428197411155947'
        key = "f40a75704fac353952a6534a18f9f437"
        a = self.shenfenzheng(cardno,key)
        assert a['reason'] == '成功的返回'
    @pytest.mark.skip('强制跳过，不需要条件')
    def test_03(self):
        cardno = '130428197411155947'
        key = "f40a75704fac353952a6534a18f9f43"
        a = self.shenfenzheng(cardno,key)
        assert  a['reason']=='错误的请求KEY'
    @pytest.mark.skipif(True,reason='条件成立时候，进行跳过')
    def test_04(self):
        cardno = '42082120031108929'
        key = "f40a75704fac353952a6534a18f9f437"
        a = self.shenfenzheng(cardno,key)
        assert a['reason'] in '请输入正确的15或18位身份证'

if __name__ == '__main__':
    pytest.main(['-s','D:\untitled20211210_01\package1\package1_01\dist\\numpypy.py'])
