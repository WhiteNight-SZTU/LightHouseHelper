#通过密钥ID、Key获取client对象
import logger

from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.lighthouse.v20200324 import lighthouse_client, models

class Client:
    __id,__key=None,None
    def login(id:str,key:str,region:str)->lighthouse_client.LighthouseClient:
        try:
            __id,__key=id,key
            cred=credential.Credential(id,key)
            client=lighthouse_client.LighthouseClient(cred,region)
            logger.info('登录成功')
            return client
        except Exception as e:
            logger.info(e)
            raise Exception('登录失败')