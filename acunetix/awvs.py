from acunetix.v11.awvs_11 import *
from config import *

class AwvsScaner:
    def __init__(self):
        self.__api_V11=AwvsApiV11(api_key=WVS_API_KEY,api_base_url=WVS_API_BASE_URL,request_timeout=WVS_API_REQUEST_TIMEOUT)

    @property
    def v11(self):
        return self.__api_V11