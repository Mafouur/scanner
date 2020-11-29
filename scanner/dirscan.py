import requests     
import time
from lib.fake_ua import headers
from rich.console import Console

console = Console()

def read_file(filepath):                               
    f = open(filepath,encoding='utf-8').readlines()     
    return f                                            


def dirs(ip):
    mulu = read_file("lib/dirdata.txt")
    for i in mulu:                                      
        mulu1 = i.strip("\n")                          
        mulu2 = mulu1.strip("/")                       
        url= ip + str(mulu2)+""
        response = requests.get(url,headers=headers)
        response2=response.url
        if response.status_code==200 and ".psp" not in response2:
            console.print("[+]  "+str(mulu2)+" 存在",style="#ADFF2F")
            with open("result.txt","a") as f:
                f.write(mulu2 + '\n')
            f.close()
        else:
            pass
    print("扫描完.结果至result.txt")
    time.sleep(0.1)

if __name__ == '__main__':
    dirs(input(":"))
