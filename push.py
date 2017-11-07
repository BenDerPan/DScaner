import requests
import json

class RestApiPusher(object):
    '''
    Rest API 数据推送工具类实现
    '''
    PUSH_URL=""
    @staticmethod
    def push(dataDic,retry=3):
        while True:
            try:
                res = requests.post(url=RestApiPusher.PUSH_URL, json=dataDic,timeout=2)
                return res.json()
            except Exception as e:
                retry-=1
                if retry<1:
                    print("[!]推送信息失败:API={0},Data={1},ErrorMsg:{2}".format(RestApiPusher.PUSH_URL, dataDic, e))
                    return None