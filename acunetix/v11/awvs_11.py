import requests
import requests.packages.urllib3
import json

# 禁用https证书相关警告
requests.packages.urllib3.disable_warnings()


class AwvsApiV11:
    PROFILE_ID_FULL_SCAN = "11111111-1111-1111-1111-111111111111"    #Full Scan   1   {"wvs": {"profile": "Default"}}
    PROFILE_ID_HIGH_RISK_VULNERABILITIES = "11111111-1111-1111-1111-111111111112"    #High Risk Vulnerabilities
    PROFILE_ID_SQL_INJECTION_VULNERABILITIES = "11111111-1111-1111-1111-111111111113"    #SQL Injection Vulnerabilities
    PROFILE_ID_CONTINUOUS_FULL = "11111111-1111-1111-1111-111111111114"   #quick_profile_1 0   {"wvs": {"profile": "continuous_full"}}
    PROFILE_ID_WEAK_PASSWORDS = "11111111-1111-1111-1111-111111111115"   #Weak Passwords
    PROFILE_ID_CROSS_SITE_SCRIPTING_VULNERABILITIES = "11111111-1111-1111-1111-111111111116"   #Cross-site Scripting Vulnerabilities
    PROFILE_ID_CRAWL_ONLY = "11111111-1111-1111-1111-111111111117"  #Crawl Only
    PROFILE_ID_CONTINUOUS_QUICK = "11111111-1111-1111-1111-111111111118"  #quick_profile_2 0   {"wvs": {"profile": "continuous_quick"}}

    REPORT_ID_DEVELOPER = "11111111-1111-1111-1111-111111111111"  # Developer
    REPORT_ID_XML = "21111111-1111-1111-1111-111111111111"  # XML
    REPORT_ID_OWASP_TOP_10 = "11111111-1111-1111-1111-111111111119"  # OWASP Top 10 2013
    REPORT_ID_QUICK = "11111111-1111-1111-1111-111111111112"  # Quick


    def __init__(self, api_key, api_base_url, request_timeout=30):
        self.__api_key = api_key
        self.__api_base_url = api_base_url
        self.__request_timeout = request_timeout
        self.targets_api_url = self.__api_base_url + "/api/v1/targets"
        self.scans_api_url = self.__api_base_url + "/api/v1/scans"
        self.reports_api_url=self.__api_base_url+ "/api/v1/reports"

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

    def start_scan(self,url,profile_id=PROFILE_ID_FULL_SCAN):
        # 先获取全部的任务.避免重复
        # 添加任务获取target_id
        # 开始扫描
        targets = self.get_running_targets()
        if url in targets:
            print('[!]任务[{0}]已经在运行中...请勿重复提交.'.format(url))
            return
        else:
            target_id = self.add_target(url)
            data = {"target_id": target_id, "profile_id": profile_id,
                    "schedule": {"disable": False, "start_date": None, "time_sensitive": False}}
            try:
                response = requests.post(self.scans_api_url, data=json.dumps(data), headers=self.auth_headers, timeout=self.__request_timeout,
                                         verify=False)
                result = response.json()
                return result['target_id']
            except Exception as e:
                print('[!]开始AWVS url={0}的扫描任务失败：{1}'.format(url, e))
                return None

    def get_all_scan(self):
        try:
            response = requests.get(self.scans_api_url, headers=self.auth_headers, timeout=self.__request_timeout, verify=False)
            results = response.json()
            return results['scans']
        except Exception as e:
            print('[!]获取所有AWVS扫描目标失败：{}'.format(e))
            return None

    def get_running_targets(self):
        allscans=self.get_all_scan()
        targets=[]
        if allscans:
            for result in allscans:
                targets.append(result['target']['address'])
                print(result['scan_id'], result['target']['address'], self.get_scan_status(result['scan_id']))
        return list(set(targets))

    def get_scan_status(self,scan_id):
        # 获取scan_id的扫描状况
        try:
            response = requests.get("{0}/{1}".format(self.scans_api_url,scan_id), headers=self.auth_headers, timeout=self.__request_timeout, verify=False)
            result = response.json()
            status = result['current_session']['status']
            return status
        except Exception as e:
            print('[!]获取AWVS scan_id={0}的扫描状况失败：{1}'.format(scan_id,e))
            return None

    def delete_scan(self,scan_id):
        # 删除scan_id的扫描
        try:
            response = requests.delete("{0}/{1}".format(self.scans_api_url,scan_id), headers=self.auth_headers, timeout=self.__request_timeout,
                                       verify=False)
            # 如果是204 表示删除成功
            if response.status_code == "204":
                return True
            else:
                return False
        except Exception as e:
            print('[!]删除AWVS scan_id={0}的扫描任务失败：{1}'.format(scan_id,e))
            return False

    def delete_target(self,target_id):
        # 删除target_id的扫描
        try:
            response = requests.delete("{0}/{1}".format(self.targets_api_url,target_id), headers=self.auth_headers, timeout=self.__request_timeout,
                                       verify=False)
            print(response.json())
            return True
        except Exception as e:
            print('[!]删除AWVS target_id={0}的扫描任务失败：{1}'.format(target_id,e))
            return False

    def stop_scan(self,scan_id):
        # 停止scan_id的扫描
        try:
            response = requests.post("{0}/{1}/abort".format(self.scans_api_url,scan_id), headers=self.auth_headers, timeout=self.__request_timeout,
                                       verify=False)
            # 如果是204 表示停止成功
            if response.status_code == "204":
                return True
            else:
                return False
        except Exception as e:
            print('[!]停止AWVS scan_id={0}的扫描任务失败：{1}'.format(scan_id,e))
            return False

    def get_reports(self,scan_id):
        # 获取scan_id的扫描报告

        data = {"template_id": AwvsApiV11.REPORT_ID_XML,
                "source": {"list_type": "scans", "id_list": [scan_id]}}
        try:
            response = requests.post(self.reports_api_url, data=json.dumps(data), headers=self.auth_headers, timeout=self.__request_timeout,
                                     verify=False)
            result = response.headers
            report = result['Location'].replace('/api/v1/reports/', '/reports/download/')
            return self.__api_base_url.rstrip('/') + report
        except Exception as e:
            print('[!]获取AWVS scan_id={0}的扫描结果报表失败：{1}'.format(scan_id, e))
            return None
        finally:
            #self.delete_scan(scan_id)
            pass

    def config_and_run(self,url,profile_id=PROFILE_ID_FULL_SCAN):
        target_id = self.add_target(url)
        # 获取全部的扫描状态
        data = {
            "excluded_paths": ["manager", "phpmyadmin", "testphp"],
            "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
            "custom_headers": ["Accept: */*", "Referer:" + url, "Connection: Keep-alive"],
            "custom_cookies": [{"url": url,
                                "cookie": "UM_distinctid=15da1bb9287f05-022f43184eb5d5-30667808-fa000-15da1bb9288ba9; PHPSESSID=dj9vq5fso96hpbgkdd7ok9gc83"}],
            "scan_speed": "moderate",  # sequential/slow/moderate/fast more and more fast
            "technologies": ["PHP"],  # ASP,ASP.NET,PHP,Perl,Java/J2EE,ColdFusion/Jrun,Python,Rails,FrontPage,Node.js
            # 代理
            "proxy": {
                "enabled": False,
                "address": "127.0.0.1",
                "protocol": "http",
                "port": 8080,
                "username": "aaa",
                "password": "bbb"
            },
            # 无验证码登录
            "login": {
                "kind": "automatic",
                "credentials": {
                    "enabled": False,
                    "username": "test",
                    "password": "test"
                }
            },
            # 401认证
            "authentication": {
                "enabled": False,
                "username": "test",
                "password": "test"
            }
        }
        try:
            res = requests.patch("{0}/{1}/configuration".format(self.targets_api_url,target_id), data=json.dumps(data),
                                 headers=self.auth_headers, timeout=self.__request_timeout, verify=False)

            return self.start_scan(url,profile_id)
        except Exception as e:
            print('[!]配置并运行AWVS url={0}扫描任务失败：{1}'.format(url, e))
            return None



if __name__ == '__main__':
    testTarget="http://testhtml5.vulnweb.com/"
    awvs=AwvsApiV11(api_key="1986ad8c0a5b3df4d7028d5f3c06e936ce3cf93e80a70434691e18edb1fd7c86f",
                    api_base_url="https://192.168.3.56:3443/")
    awvs.test()
    # target_id=awvs.add_target(testTarget,"测试目标")
    # if target_id:
    #     print("[*]成功添加目标[{0}],target_id={1}".format(testTarget,target_id))

    scan_id=awvs.start_scan(url=testTarget,profile_id=AwvsApiV11.PROFILE_ID_HIGH_RISK_VULNERABILITIES)
    if scan_id:
        print(scan_id)

    scan_id="4d52815e-59df-4fd7-9914-3ccb6428bc59"
    runnings=awvs.get_running_targets()
    status=awvs.get_scan_status(scan_id)
    report=awvs.get_reports(scan_id)
    print(report)
