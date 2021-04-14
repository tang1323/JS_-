import random
import time


import requests
import re


target_urls = "http://zwfw.san-he.gov.cn/icity/icity/guestbook/interact#"

"""
如果在headers里面有set_cookies
那这个cookies就和首页有cookies是一样的
获取cookies就是向首页发起请求。然后获取cookies"""
response = requests.get(target_urls)
# 需要获取cookies才能爬取数据
# print(response.cookies['ICITYSession'])
# print(response.text)
res = response.text
# print(res)
# 获取sig值，在首页，用正则取出，在__signature中
text_re = "__signature = \"(.*)\""
match_obj = re.search(text_re, res)
sig = match_obj.group(1)
print("这是sig值：", sig)



# 现在我们根据下面的js语句要用python来伪造key和t

# sig = "b580221608303975662"
key = ""
keyindex = -1
chars = "0123456789abcdef"
for i in range(0, 6):
    c = sig[keyindex + 1]
    key += c
    keyindex = chars.index(c)
    if keyindex < 0 and keyindex >= len(sig):
        keyindex = i
print("这是key值：", key)



# 现在来伪造下面的t
t = str(int(random.randint(999, 10000))) + "_" + key + "_" + str(int(time.time()))+"000"
ts = t.replace("+", "_")
print("这是t值", ts)
"""
s: d134791608286542429
t: 1655_d49249_1608287677000
"""
# # s, t
# print(str(int(time.time())) + "000")

# 这是第一页的url
# http://zwfw.san-he.gov.cn/icity/api-v2/app.icity.guestbook.WriteCmd/getList?s=a486961608304992802&t=4905_a04666_1608305024000

# 这是第二页的url，总结，我们就是要伪造s和t的值
# http://zwfw.san-he.gov.cn/icity/api-v2/app.icity.guestbook.WriteCmd/getList?s=a486961608304992802&t=6014_a04666_1608305202000