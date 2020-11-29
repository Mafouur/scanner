import hashlib
import json
import requests
from lib.fake_ua import headers
from rich.console import Console

console = Console()
headers = headers

def getmd5(hash):
    md5 = hashlib.md5()
    md5.update(hash)
    return md5.hexdigest()

def md5_check(url,path,match_pattern,cms_name):
    try:
        r = requests.get(url+path, headers=headers, timeout=3, verify=False)
        if match_pattern == getmd5(r.content):
            return cms_name
    except:
        pass


def keyword_check(url,path,match_pattern,cms_name):
    try:
        r = requests.get(url+path, headers=headers, timeout=3, verify=False)
        if match_pattern in r.text:
            return cms_name
    except:
        pass



def Whatcms(url):
    fr = open('lib/cmsdata.json','r', encoding='UTF-8')
    data= json.load(fr, encoding='utf-8')
    fr.close()
    console.print('指纹加载成功：{}条'.format(len(data)),style="#ADFF2F")
    for i in data:
        if i['options']=='md5':
            res=md5_check(url,i['path'],i['match_pattern'],i['cms_name'])
            if res:
                console.print('目标指纹：'+res,style="#ADFF2F")
                break
        elif i['options']=='keyword':
            res=keyword_check(url,i['path'],i['match_pattern'],i['cms_name'])
            if res:
                console.print('目标指纹：'+res,style="#ADFF2F")
                break
        else:
            console.print('?',style="#ADFF2F")



if __name__ == '__main__':
    #Whatcms('http://www.dedecms.com/')
    Whatcms(input("url :"))