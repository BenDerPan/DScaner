from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import create_engine
from acunetix.v11.db.tables.targets import TargetsTable
from acunetix.v11.db.tables.target_vulns import TargetVulnsTable,TargetVulnRow
from acunetix.v11.db.tables.vuln_types import VulnTypesTable,VulnTypeRow
from config import *

class DBHelper:
    def __init__(self,host=WVS_POSTGRESQL_HOST,port=WVS_POSTGRESQL_PORT,user=WVS_POSTGRESQL_USER,pwd=WVS_POSTGRESQL_PWD,db_name=WVS_POSTGRESQL_DB_NAME):
        self.__host=host
        self.__port=port
        self.__user=user
        self.__pwd=pwd
        self.__db_name=db_name
        self.__engine=self.__create_engine()
        self.__session=self.__create_session()

    def __create_engine(self):
        return create_engine('postgresql+psycopg2://{0}:{1}@{2}:{3}/{4}'.format(self.__user,self.__pwd,self.__host,self.__port,self.__db_name))

    def __create_session(self):
        return sessionmaker(bind=self.__engine)()

    @property
    def session(self):
        return self.__session

    def get_targets(self):
        targets=None
        try:
            targets=self.session.query(TargetsTable)
        except Exception as e:
            print('[!]获取目标列表失败：{}'.format(e))
            targets=None
        finally:
            return targets

    def get_target_vulns(self,target_id):
        vulns = None
        try:
            vulns = self.session.query(TargetVulnsTable).filter(TargetVulnRow.target_id==target_id)
        except Exception as e:
            print('[!]获取目标漏洞列表列表失败：{}'.format(e))
            vulns = None
        finally:
            return vulns

    def get_vuln_type(self,vt_id):
        vulns_type = None
        try:
            vulns_type = self.session.query(VulnTypesTable).filter(VulnTypeRow.vt_id==vt_id)
        except Exception as e:
            print('[!]获取漏洞详情信息失败：{}'.format(e))
            vulns_type = None
        finally:
            return vulns_type


if __name__ == '__main__':
    dbHelper=DBHelper(port=35432)
    targets=dbHelper.get_targets()
    vuls=dbHelper.get_target_vulns("87bd9c89-3511-48f1-bbda-2b69e3bddb00")
    for v in vuls:
        print(v.vt_id)

    for target in targets:
        vuls=dbHelper.get_target_vulns(target.target_id)
        for v in vuls:
            vul=dbHelper.get_vuln_type(v.vt_id)
            print(vul)
    for instance in dbHelper.session.query(TargetsTable):
        print(instance.target_id, instance.description)
