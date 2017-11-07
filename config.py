CELERY_TASK_NAME = "tasks"
CELERY_BROKER = "redis://localhost:6379/0"
CELERY_BACKEND = "redis://localhost:6379/1"

WVS_POSTGRESQL_HOST = "localhost"
WVS_POSTGRESQL_PORT = 35432
WVS_POSTGRESQL_USER = "wvs"
WVS_POSTGRESQL_PWD = "wvs"
WVS_POSTGRESQL_DB_NAME = "wvs"

WVS_API_KEY = "1986ad8c0a5b3df4d7028d5f3c06e936ce3cf93e80a70434691e18edb1fd7c86f"
WVS_API_BASE_URL = "https://localhost:3443/"
WVS_API_REQUEST_TIMEOUT = 30

# Sqlite数据后端
STORAGE_BACKEND = "sqlite:///awvs.db"

# Mysql数据后端
# STORAGE_BACKEND="mysql://user:pwd@localhost/db"

#推送漏洞数据API接口
VULN_PUSH_API_URL="http://localhost/api/vulns"
ENABLE_VULN_PUSH=False
