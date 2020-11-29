import os
import nmap
#from nmap import nmap
from rich.console import Console

console = Console()

def nmap_scan(ips):
    a = ips.split(':')
    print(a)
    ip = a[0]
    port = a[1]
    nm = nmap.PortScanner()
    nm.scan(hosts=ip,ports=port)

    for host in nm.all_hosts():#主机列表
        print('-----------------------------------------------------------')
        console.print('Host : %s -%s' % (host, nm[host].hostname()),style="#ADFF2F") #打印主机名
        #print('State : %s' % nm[host].state()) #主机状态
        for proto in nm[host].all_protocols(): #端口协议列表
            #print('Protocol : %s' % proto) #打印端口协议
            lport = sorted(nm[host][proto].keys()) #可迭代的对象进行排序 端口排序 
            for port in lport: #端口列表
                console.print('端口 : %s \n服务 : %s' % (port, nm[host][proto][port]['name']),style="#1B7565")
                console.print('软件 : %s' % (nm[host][proto][port]['product']),style="#1B7565")
                console.print('版本号 : %s' % (nm[host][proto][port]['version']),style="#1B7565")
                console.print('-----------------------------------------------------------',style="#F9C450")

if __name__ == "__main__":
    nmap_scan(input("ip:"))
