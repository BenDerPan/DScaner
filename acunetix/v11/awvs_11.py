import requests
import requests.packages.urllib3
import json

# 禁用https证书相关警告
requests.packages.urllib3.disable_warnings()


class AwvsApiV11:
    PROFILE_ID_FULL_SCAN = "11111111-1111-1111-1111-111111111111"
    PROFILE_ID_HIGH_RISK_VULNERABILITIES = "11111111-1111-1111-1111-111111111112"
    PROFILE_ID_SQL_INJECTION_VULNERABILITIES = "11111111-1111-1111-1111-111111111113"
    PROFILE_ID_CONTINUOUS_FULL = "11111111-1111-1111-1111-111111111114"
    PROFILE_ID_WEAK_PASSWORDS = "11111111-1111-1111-1111-111111111115"
    PROFILE_ID_CROSS_SITE_SCRIPTING_VULNERABILITIES = "11111111-1111-1111-1111-111111111116"
    PROFILE_ID_CRAWL_ONLY = "11111111-1111-1111-1111-111111111117"
    PROFILE_ID_CONTINUOUS_QUICK = "11111111-1111-1111-1111-111111111118"

    def __init__(self, api_key, api_base_url, request_timeout=30):
        self.__api_key = api_key
        self.__api_base_url = api_base_url
        self.__request_timeout = request_timeout
        self.targets_api_url = self.__api_base_url + "/api/v1/targets"
        self.scans_api_url = self.__api_base_url + "/api/v1/scans"

    @property
    def auth_headers(self):
        return {"X-Auth": self.__api_key, "content-type": "application/json"}

    def add_target(self, url, description=None, criticality=10):
        '''
        添加扫描目标
        :param url: 目标URL地址
        :param description: 任务描述
        :param criticality: 危险程度;范围:[30,20,10,0];默认为10
        :return: 成功返回目标ID，失败范围None
        '''
        if not description:
            description = url
        data = {"address": url, "description": description, "criticality": criticality}
        try:
            response = requests.post(self.targets_api_url, data=json.dumps(data),
                                     headers=self.auth_headers, timeout=self.__request_timeout,
                                     verify=False)
            result = response.json()
            return result['target_id']
        except Exception as e:
            print('[!]添加扫描目标到AWVS失败：{}'.format(e))
            return None
