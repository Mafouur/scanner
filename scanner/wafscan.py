import requests
import re
from lib.wafdata import WAF_RULE

def verify(headers, content):
    for i in WAF_RULE:
        name, method, position, regex = i.split('|')
        if method == 'headers':
            if headers.get(position) is not None:
                if re.search(regex, str(headers.get(position))) is not None:
                    return name
        else:
            if re.search(regex, str(content)):
                return name
    return 'NoFountWAF'


def checkwaf(url):
    payload = ('/index.php?id=1 and 1=1')#,'/phpinfo.php')#'/../../../etc/passwd','/.git/',)
    #result = 'NoWAF'
    print(url)
    try:
        r = requests.get(url)
        result = verify(r.headers, r.text)
        if result == 'NoFountWAF':
            r = requests.get(url + payload)
            result = verify(r.headers, r.text)
            if result != 'NoFountWAF':
                print("waf:",result)
        else:
            print("waf:",result)
    except (UnboundLocalError, AttributeError):
        pass
    except Exception as e:
        print('error')


if __name__ == "__main__":
    checkwaf(input("URL:"))


