import argparse
#from scanner
from scanner.wafscan import checkwaf
from scanner.wafscan import verify
from scanner.portscan import pscan
from scanner.test import domain
from scanner.test import xinxi
from scanner.nmm import nmap_scan
from lib import banner
from scanner.cmscan import Whatcms
from scanner.dirscan import dirs
from rich.console import Console

console = Console()

def xx():
    parser = argparse.ArgumentParser(description='参数说明.')
    parser.add_argument("-w","--wafscan",help="waf扫描",dest='waf')
    parser.add_argument("-p","--portscan",help="端口扫描",dest='port')#,action="store_true")
    parser.add_argument("-d","--domainscan",help="子域名扫描",dest="domain")
    parser.add_argument("-o","--whois",help="whois查询",dest="whois")
    parser.add_argument("-n","--nmap",help="nmap扫描,多个ip用空格分隔,多个端口用','分隔,ip跟端口之间用':'分隔",dest="nmap")
    parser.add_argument("-dirscan",help="敏感目录扫描,like(https://baidu.com/)",dest="dirscan")
    parser.add_argument("-cmscan",help="CMS扫描,like(https://baidu.com/)",dest="cmscan")
    parser.add_argument("-pksb",dest="pksb")
    args = parser.parse_args()
    if args.waf:
        checkwaf(args.waf)
    elif args.port:
        pscan(args.port)
    elif args.domain:
        domain(args.domain)
    elif args.whois:
        xinxi(args.whois)
    elif args.nmap:
        nmap_scan(args.nmap)
    elif args.dirscan:
        dirs(args.dirscan)
    elif args.cmscan:
        Whatcms(args.cmscan)
    elif args.pksb:
    	console.print("或许你想要这个(。・∀・)ノ=>(https://i0.hdslb.com/bfs/album/4b071a36dc6d00d2a3dd2e171b501801477398a0.jpg)",style="#008080")
    else:
        console.print("你好呀",style="#EE82EE")
    

        
    #elif args.port:
    #    portscan(args.ip)


if __name__ == "__main__":
    xx()
