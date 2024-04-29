import logger 
from tencentcloud.lighthouse.v20200324 import lighthouse_client, models
from lib.snapshot import SnapshotAPI
class Menu:
    __client=None
    __snapshot=None
    def __init__(self,client:lighthouse_client.LighthouseClient):
        self.__client=client
        self.__snapshot=SnapshotAPI()
        self.show_menu()
        
    def show_menu(self):
        while True:
            print("轻量服务器自动化脚本")
            print('1.快照')
            print('0.退出')
            choice=input("请输入选项序号：")
            if choice=='1':
                self.__snapshot_menu()
            elif choice=='0':
                logger.info("退出")
                break
        
    def __snapshot_menu(self):
        print("1.获取快照列表")
        print("0.返回上一级")
        choice=input("请输入选项序号：")
        if choice == '1':
            self.__snapshot.get_snapshot_list(self.__client)
        elif choice == '0':
            return