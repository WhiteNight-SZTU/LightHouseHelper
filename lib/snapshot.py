from tencentcloud.lighthouse.v20200324 import lighthouse_client, models
import json
import logger
import time
from lib.instance import InstanceAPI
class SnapshotAPI:
    __instance=None
    def __init__(self):
        self.__instance=InstanceAPI()
        
    def __get_snapshot_from_resp(self,resp):
        if resp is None:
            logger.info("无快照")
            return []
        snapshot_list=[]
        for snapshot in resp.SnapshotSet:
            snapshot_list.append({
                'SnapshotId':snapshot.SnapshotId,
                'SnapshotName':snapshot.SnapshotName,
                'CreatedTime':snapshot.CreatedTime.split('T')[0]+' '+snapshot.CreatedTime.split('T')[1].split('Z')[0],
                'DiskUsage':snapshot.DiskUsage,
            })
        return snapshot_list
    
    def get_snapshot_list(self,client:lighthouse_client.LighthouseClient):
        try:
            resp=models.DescribeSnapshotsRequest()
            params={}
            resp.from_json_string(json.dumps(params))
            resp=client.DescribeSnapshots(resp)
        except Exception as e:
            logger.error('获取快照列表失败')
            logger.error(e)
        snapshot_list=self.__get_snapshot_from_resp(resp)
        logger.info('获取快照列表成功')
        for snapshot in snapshot_list:
            print('快照ID：{}'.format(snapshot['SnapshotId'])+' 名称：{}'.format(snapshot['SnapshotName'])+' 创建时间：{}'.format(snapshot['CreatedTime']))
        logger.debug(snapshot_list)
        return snapshot_list
    
    def create_snapshot(self,client:lighthouse_client.LighthouseClient):
        available_instance_list=[]
        try:
            available_instance_list=self.__instance.get_instance_list(client)
            logger.info("获取实例列表成功")
            for ins in available_instance_list:
                print("序号：{} 实例ID：{} 实例名称：{}".format(available_instance_list.index(ins),ins['InstanceId'],ins['InstanceName']))
        except Exception as e:
            logger.error('获取实例列表失败')
            logger.error(e)
        choice=input("请输入实例序号：")
        try:
            ins=available_instance_list[int(choice)]
            snapshot_name="Snapshot-"+str(time.strftime("%Y%m%d%H%M%S", time.localtime()))
            logger.info('新建快照：'+' 名称：{}'.format(snapshot_name))
            req=models.CreateInstanceSnapshotRequest()
            params={
                "InstanceId":ins['InstanceId'],
                "SnapshotName":snapshot_name
            }
            req.from_json_string(json.dumps(params))
            resp=client.CreateInstanceSnapshot(req)
            logger.debug(resp.to_json_string())
            logger.info('新建快照成功')
        except Exception as e:
            logger.error('新建快照失败')
            logger.error(e)
