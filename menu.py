import logger 
from tencentcloud.lighthouse.v20200324 import lighthouse_client, models
from lib.snapshot import SnapshotAPI
from lib.instance import InstanceAPI
class Menu:
    __client=None
    __snapshot=None
    __instance=None
    def __init__(self,client:lighthouse_client.LighthouseClient):
        self.__client=client
        self.__snapshot=SnapshotAPI()
        self.__instance=InstanceAPI()
        self.show_menu()
        
    def show_menu(self):
        while True:
            print("轻量服务器自动化脚本")
            print('1.快照')
            print("2.实例")
            print('0.退出')
            choice=input("请输入选项序号：")
            if choice=='1':
                self.__snapshot_menu()
            elif choice=='2':
                self.__instance_menu()
            elif choice=='0':
                logger.info("退出")
                break
    
    def __instance_menu(self):
        print("1.获取实例列表")
        print("0.返回上一级")
        choice=input("请输入选项序号：")
        if choice == '1':
            self.__instance.get_instance_list(self.__client)
        elif choice == '0':
            return
    
    def __snapshot_menu(self):
        print("1.获取快照列表")
        print("2.新建快照")
        print("0.返回上一级")
        choice=input("请输入选项序号：")
        if choice == '1':
            self.__snapshot.get_snapshot_list(self.__client)
        elif choice == '2':
            self.__snapshot.create_snapshot(self.__client)
        elif choice == '0':
            return