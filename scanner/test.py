#coding=utf-8
import re
import requests
from lib.fake_ua import headers



def domain(yum):
        print ("[+]子域名收集模块已开启.")
        sites = []
        url = 'https://chaziyu.com/'+ yum   #设定url请求
        response = requests.get(url,headers=headers).text   #get请求，content获取返回包正文
        #print(response)
        ipchaxun = re.findall(r'target="_blank">(.*?)</',response)
        #zhaokuaizhao = re.findall(r'rel="nofollow">(.*?)</',response) 
        #print(ipchaxun)
        #print(zhaokuaizhao)
        sites += list(ipchaxun)# + zhaokuaizhao) 
        site = list(set(sites))  #set()实现去重
        # print site
        print ("\n一共有 %d 子域名。" %len(site)+"\n")
        for i in site:
            print(i)




def xinxi(yum):
        print ("[+]信息收集模块开启.")
        #sts = ()
        url ="http://whois.chinaz.com/"+ yum#str(text)
        response = requests.get(url).text#content.decode('utf-8')  # get请求，content获取返回包正文
        baidudomain = re.findall(r'<div class="block ball"><span>(.*?)</', response)  ##注册商
        xiang = re.findall(r'<div class="fr WhLeList-right block ball lh24"><span>(.*?)</', response)  ##邮箱和联系电话
        dns = re.findall(r'<div class="fr WhLeList-right"><span>(.*?)</', response)  ##dns
        #print(sts())
        print ("\n")
        print ("/==============================\\")
        print ("|------------注册商------------:=>>",">>",baidudomain)
        print ("|-------注册人邮箱++++电话-----:=>>",">>",xiang)
        print ("|-域名注册时间++++域名到期时间-:=>>",">>",dns)#.decode('utf-8'))#"string_escape"))
        print ("\==============================/")



if __name__ == '__main__':
        yum = input('请输入不带http:// 的url  如 qq.com \n url:')
        domain(yum)  ##子域名收集模块开启
        print ("\n")
        xinxi(yum)   ##信息收集模块开启
