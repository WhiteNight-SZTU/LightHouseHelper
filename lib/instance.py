from tencentcloud.lighthouse.v20200324 import lighthouse_client, models
import json
import logger

class InstanceAPI:
    def __get_instance_from_resp(self,resp):
        if resp is None:
            logger.info("无实例")
            return []
        instance_list=[]
        for instance in resp.InstanceSet:
            instance_list.append({
                "InstanceId":instance.InstanceId,
                "InstanceName":instance.InstanceName,
                "InstanceState":instance.InstanceState,
                "CPU":instance.CPU,
                "Memory":instance.Memory,
                "SystemDisk":instance.SystemDisk,
                "PrivateAddresses":instance.PrivateAddresses,
                "PublicAddresses":instance.PublicAddresses,
                "Uuid":instance.Uuid,
                "CreatedTime":instance.CreatedTime.split('T')[0]+' '+instance.CreatedTime.split('T')[1].split('Z')[0],
                "ExpiredTime":instance.ExpiredTime.split('T')[0]+' '+instance.ExpiredTime.split('T')[1].split('Z')[0],
                "OsName":instance.OsName,
                "Zone":instance.Zone,
            })
        return instance_list
    
    def get_instance_list(self,client:lighthouse_client.LighthouseClient):
        try:
            req=models.DescribeInstancesRequest()
            params={}
            req.from_json_string(json.dumps(params))
            resp=client.DescribeInstances(req)
        except Exception as e:
            logger.error('获取实例列表失败')
            logger.error(e)
        instance_list=self.__get_instance_from_resp(resp)
        logger.debug(instance_list)
        return instance_list

    