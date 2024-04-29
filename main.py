import argparse
import logger
from login import Client
from menu import Menu 

from lib.snapshot import SnapshotAPI

def parse():
    parser = argparse.ArgumentParser("LightHosueHelp",description="轻量服务器自动化脚本")
    parser.add_argument("--id",help="密钥ID")
    parser.add_argument("--key",help="密钥KEY")
    parser.add_argument("--log",default="info",help="日志等级，默认info，可选debug")
    parser.add_argument("--region",default="ap-guangzhou",help="地域,默认ap-guangzhou")
    parser.add_argument("--debug",default='False',help="调试模式,默认False")
    parser.add_argument("--snapshot",default=None,help="快照模式，默认None，可选delete,create,check")
    return parser.parse_args()

def main():
    args=parse()
    logger.set_logger(args.log)
    logger.debug(args)
    client=Client.login(args.id,args.key,args.region)
    if args.debug == 'True' or args.debug == 'true':
        fast(args,client)
    menu=Menu(client)
    
def fast(args,client):
    if args.snapshot is not None:
        snapshot_api=SnapshotAPI()
        if args.snapshot == "check":
            snapshot_api.get_snapshot_list(client)
    exit(0)
if __name__=="__main__":
    main()