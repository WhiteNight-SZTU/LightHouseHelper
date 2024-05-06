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
    
    def get_instance_list(self,client:lighthouse_client.LighthouseClient,print_list:False):
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
        if print_list:
            for instance in instance_list:
                print("拥有实例列表：")
                print("序号：{} 实例ID：{} 实例名称：{} 实例状态：{} 实例CPU：{}核 实例内存：{}G 系统盘：{} 私有IP：{} 公有IP：{} UUID：{} 创建时间：{} 过期时间：{} 操作系统：{} 可用区：{}".format(instance_list.index(instance),instance['InstanceId'],instance['InstanceName'],instance['InstanceState'],instance['CPU'],instance['Memory'],instance['SystemDisk'],instance['PrivateAddresses'],instance['PublicAddresses'],instance['Uuid'],instance['CreatedTime'],instance['ExpiredTime'],instance['OsName'],instance['Zone']))
        return instance_list

    