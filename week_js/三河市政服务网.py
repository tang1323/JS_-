

import requests
import re


target_urls = "http://zwfw.san-he.gov.cn/icity/icity/guestbook/interact#"

"""
如果在headers里面有set_cookies
那这个cookies就和首页有cookies是一样的
获取cookies就是向首页发起请求。然后获取cookies"""
# response = requests.get(target_urls)
# # 需要获取cookies才能爬取数据
# # print(response.cookies['ICITYSession'])
# # print(response.text)
# res = response.text
# # print(res)

# # 获取sig值，在首页，用正则取出，在__signature中
# text_re = "__signature = \"(.*)\""
# match_obj = re.search(text_re, res)
# if match_obj:
#     print(match_obj.group(1))
#
#
#
# exit()
# 这个网站有点debug，但是有的网站是无限debug





headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36 Edg/80.0.361.111'
}
"""
这个是在start_url后面的，很明显看到t字段有变化
在__signature字段也是s的值，通过打印首页html
s: d134791608286542429
t: 8232_d49249_1608287915000

curUrl += "?s=" + sig;
curUrl += "&t=" + t;

s: d134791608286542429
t: 1655_d49249_1608287677000

先把s拿到search搜索一下
但是s在文件里肯定有很多的，那怎么样查？
用js语法：var s
这是js定义变量的，而这个s肯定是个参数，而参数肯定是一个变量里
"""
data = {
    "start": 0,
    "limit": 7,
    "TYPE@=": "2",
    "OPEN@=": "1"
}

"""
sig的python实现
sig = ""
chars = "0123456789abcdef"
curTime = str(int(random.randint(999, 10000))) + "" + time.time()
sig = chars[str(int(random.randint(0, 11))) + chars[len(curTime)]] + "" + curTime


打断点获取到js代码
var sig = "";
var chars = "0123456789abcdef";
if (!LEx.isNotNull(__signature)) {
    var curTime = parseInt(Math.random() * (9999 - 1000 + 1) + 1000) + "" + Date.parse(new Date());
    sig = chars.charAt(parseInt(Math.random() * (15 - 15 + 1) + 10)) + chars.charAt(curTime.length) + "" + curTime;
} else {
    sig = __signature;
}

现在我们根据下面的js语句要用python来伪造key和t
key = ""
keyindex = -1
chars = "0123456789abcdef"
for i in range(0, 6):
    c = sig[keyindex + 1]
    key += c
    chars.index(c)
    if keyindex < 0 and keyindex >= len(sig):
        keyindex = i
        
现在来伪造下面的t        
t = str(int(random.randint(999, 10000))) + "_" + key + "_" + 'time.time()'+000
t.replace("+", "_")
s, t
    
    
    
var key = "";
var keyIndex = -1;
for (var i = 0; i < 6; i++) {
    var c = sig.charAt(keyIndex + 1);charAt就是索引下标
    key += c;
    keyIndex = chars.indexOf(c);
    if (keyIndex < 0 || keyIndex >= sig.length) {
        keyIndex = i;
    }
}

现在来伪造下面的t
t = str(int(random.randint(999, 10000))) + "_" + key + "_" + 'time.time()'+000
t.replace("+", "_")



var timestamp = parseInt(Math.random() * (9999 - 1000 + 1) + 1000) + "_" + key + "_" + Date.parse(new Date());
var t = timestamp;
//LEx.azdg.encrypt(timestamp,key);
t = t.replace(/\+/g, "_");在js中，把+替换成_
curUrl += "?s=" + sig;
curUrl += "&t=" + t;
}
"""


def requests_sha():
    for page in range(0, 71, 7):
        start_url = "http://zwfw.san-he.gov.cn/icity/api-v2/app.icity.guestbook.WriteCmd/getList?s=ea64231608306297963&t=5165_e70a0a_1608306323000"
        response = requests.post(url=start_url, headers=headers, json=data)
        print(response.json())
        print("*" * 20)


requests_sha()

"""
第一页：{"start":0,"limit":7,"TYPE@=":"2","OPEN@=":"1"}
第二页：{"start":7,"limit":7,"TYPE@=":"2","OPEN@=":"1"}
第三页：{"start":14,"limit":7,"TYPE@=":"2","OPEN@=":"1"}

"""
















