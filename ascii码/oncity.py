

import requests
import re
"""
这个网站如果cookies失效，那就返回一些dd字段给你
而cookies里面正好有一个aa字段，经过分析，正是失效后返回的dd字段，不过是倒过来的
而正是dd字段对应ascli码的48-57->0-9  97-102->a-f
所以先故意访问不到这个网站，用re, 得到这个dd字段，而这里的cookies是dd字段倒过来的
但是这个网站封ip很历害
"""

IP_Addr = "http://114.219.157.215:8000/proxy/checked/get_next"

def get_ip():
    ip_json = requests.get(IP_Addr)
    ip = ip_json.json()['data']
    return ip


def get_aa():
    url = 'http://bbs.oncity.cc/forum-5-1.html'
    headers = {
        'User-Agent': ''
    }
    p = get_ip()
    response = requests.get(url, headers=headers, proxies=p)
    print(response.text)
    aa = re.findall(r'dd=\[(.*?)\];', response.text)[0].split(',')
    del aa[-1]
    l = []
    for a in aa:
        l.append(int(a))
    ck = ''
    for i in l:
        ck = chr(i) + ck

    return ck, p


def request():
    aa, p = get_aa()
    print(aa)
    url = "http://bbs.oncity.cc/forum-5-1.html"

    headers = {
        'User-Agent': '',
        'Cookie': 'aa={}'.format(aa),
    }

    response = requests.get(url, headers=headers, proxies=p)
    print('='*20)
    print(response.text)
























