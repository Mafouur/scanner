import socket
import ipaddr
import datetime
from concurrent.futures import ThreadPoolExecutor, wait
from rich.console import Console

console = Console()

def ip_port(ip,port):
    sockect = socket.socket()
    try:
        sockect.settimeout(0.2)
        sockect.connect((ip,port))
        if ip != ipandaddr(ip):
            console.print("[+]%s(%s) open %s"%(ip,ipandaddr(ip),port),style="#ADFF2F")
        else:
            console.print("[+]%s open %s"%(ip,port),style="#ADFF2F")
    except:
        sockect.close()


def ipandaddr(ipa):
    result = socket.getaddrinfo(ipa, None)
    return result[0][4][0]


def pscan(ip):
    while True:
        #ip = input("请输入ip地址 or 域名:")
        print('扫描:%s'% (ipandaddr(ip)))
        if ipandaddr(ip):
            start_time = datetime.datetime.now()
            executor = ThreadPoolExecutor(max_workers=600)
            t = [executor.submit(ip_port,ip,n) for n in range(1, 65536)]
            if wait(t, return_when='ALL_COMPLETED'):
                end_time = datetime.datetime.now()
                print("扫描完成,用时:", (end_time - start_time).seconds,"s")
                break

if __name__ == '__main__':
    pscan(input("请输入ip地址 or 域名:"))
    #ipandaddr(input(":"))

